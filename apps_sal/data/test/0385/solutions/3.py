def preproc(str, leng):
    li = []
    res = [-1] * leng
    for i in range(leng):
        if str[i] == '(':
            li.append(i)
        else:
            start, end = li.pop(), i
            res[start] = end
            res[end] = start
    return res


def delete(flags, cursor, pairs):
    pos = pairs[cursor]
    direction = 1 if pos > cursor else -1
    while(pos + direction > 0 and pos + direction < len(flags) and flags[pos + direction] != -1):
        pos = flags[pos + direction]
    return pos


leng, op_num, cursor = map(int, input().strip().split())
cursor = cursor - 1
str = input().strip()
ops = input().strip()
pairs = preproc(str, leng)
flags = [-1] * leng
#print(leng, op_num, cursor, str, ops, pairs)
for i in ops:
    #print(i, cursor, flags)
    if i == 'R' or i == 'L':
        cursor = {
            'R': (lambda cursor=cursor, flags=flags: cursor + 1 if flags[cursor + 1] == -1 else flags[cursor + 1] + 1),
            'L': (lambda cursor=cursor, flags=flags: cursor - 1 if flags[cursor - 1] == -1 else flags[cursor - 1] - 1)
        }[i]()
    else:
        delete_to = delete(flags, cursor, pairs)
        delete_from = delete(flags, pairs[cursor], pairs)
        flags[delete_from] = delete_to
        flags[delete_to] = delete_from
        cursor = max(delete_to, delete_from)
        if cursor + 1 < leng and flags[cursor + 1] == -1:
            cursor = cursor + 1
        elif cursor + 1 < leng and flags[cursor + 1] != -1 and flags[cursor + 1] + 1 < leng:
            cursor = flags[cursor + 1] + 1
        elif min(delete_from, delete_to) - 1 > 0 and flags[min(delete_from, delete_to) - 1] == -1:
            cursor = min(delete_from, delete_to) - 1
        else:
            cursor = flags[min(delete_from, delete_to) - 1] - 1
idx = 0
res = ''
while idx < leng:
    if flags[idx] != -1:
        idx = flags[idx] + 1
        continue
    res += str[idx]
    idx = idx + 1
print(res)
