"""
必要十分条件
１）Sの中の同じ文字が、Tの別の文字に対応していない
２）Tの中の同じ文字が、Sの別の文字に対応していない
"""

s = input()
t = input()

dict_st = {}
dict_ts = {}

for x, y in zip(s, t):
    if x not in dict_st:
        dict_st[x] = y
    else:
        if dict_st[x] != y:
            print('No')
            break
    
    if y not in dict_ts:
        dict_ts[y] = x
    else:
        if dict_ts[y] != x:
            print('No')
            break
else:
    print('Yes')

