n = int(input())
list_s = [input() for i in range(0, n)]
m = int(input())
list_t = [input() for i in range(0, m)]
dict_blue = {}
dict_red = {}
list_ans = []
for i in range(0, n):
    if list_s[i] in dict_blue:
        pass
    else:
        dict_blue[list_s[i]] = list_s.count(list_s[i])
for i in range(0, m):
    if list_t[i] in dict_red:
        pass
    else:
        dict_red[list_t[i]] = list_t.count(list_t[i])
for key, value in dict_blue.items():
    if key in dict_red.keys():
        list_ans.append(value - dict_red[key])
    else:
        list_ans.append(value)
if max(list_ans) > 0:
    print(max(list_ans))
else:
    print(0)
