s = input()
t = input()
dict_st = {}
dict_ts = {}
for (x, y) in zip(s, t):
    if x not in dict_st:
        dict_st[x] = y
    elif dict_st[x] != y:
        print('No')
        break
    if y not in dict_ts:
        dict_ts[y] = x
    elif dict_ts[y] != x:
        print('No')
        break
else:
    print('Yes')
