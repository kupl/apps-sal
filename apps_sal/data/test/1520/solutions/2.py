n = input()
n = int(n)
p = []
substring_maxlen = 0
str_info = []

_temper = [
    "abba", "a"
]

for i in range(n):
    string = input()
    str_info.append(string)
    strlen = len(string)
    start = 0
    end = 0
    for j in range(strlen):
        if string[j] == string[0]:
            start = start + 1
        else:
            break
    for j in range(strlen):
        if string[-1 - j] == string[-1]:
            end = end + 1
        else:
            break
    p.append((string[0], start, string[-1], end, True if strlen == start else False))
_max_len = 0
parse = 0

_temp_max = 0
string = str_info[-1]
token = string[0]
while parse < len(string):
    token = string[parse]
    _temp_max = 0
    for k in range(parse, len(string)):
        if string[k] == token:
            parse = parse + 1
            _temp_max = _temp_max + 1
        else:
            break
    if substring_maxlen < _temp_max:
        substring_maxlen = _temp_max

start_token = []
end_token = []
start_token, start_num, end_token, end_num, connected = p[-1]
level = 0
for i in range(1, len(p)):
    if not connected:
        break
    else:
        _string = str_info[-i - 1]
        _max_len = 0
        parse = 0
        _temp_max = 0
        token = _string[0]
        _substring_maxlen = 0
        while parse < len(_string):
            token = _string[parse]
            if token != start_token:
                parse = parse + 1
                continue
            _temp_max = 0
            for k in range(parse, len(_string)):
                if _string[k] == token:
                    parse = parse + 1
                    _temp_max = _temp_max + 1
                else:
                    break
            if _substring_maxlen < _temp_max:
                _substring_maxlen = _temp_max
        substring_maxlen = max(substring_maxlen, start_num * (_substring_maxlen + 1) + _substring_maxlen)

        _start_token, _start_num, _end_token, _end_num, _connected = p[-1 - i]
        if _start_token == start_token:
            start_num = start_num * (_start_num + 1) + _start_num
        if _end_token == end_token:
            end_num = end_num * (_end_num + 1) + _end_num
        if not _connected or _start_token != start_token:
            connected = False
        level = i
end_cond = 0
if start_num > end_num:
    end_cond = 1
elif start_num < end_num:
    end_cond = 2
the_End = False
answer = max(start_num, end_num) + 1
for i in range(len(p) - level - 1):
    for s in str_info[i]:
        if start_token == s:
            if end_cond < 2:
                the_End = True
                if start_token == end_token:
                    answer = answer + min(start_num, end_num)
                break
        if end_token == s:
            if end_cond % 2 == 0:
                the_End = True
                if start_token == end_token:
                    answer = answer + min(start_num, end_num)
                break
    if the_End:
        break
else:
    answer = answer - 1
if len(p) == 1:
    answer = answer - 1

print(max(answer, substring_maxlen))
