from collections import Counter

n = int(input())
names = ['Kuro', 'Shiro', 'Katie']
s, sc = [], []
for i in range(3):
    s.append(input())
    sc.append(Counter(s[i]).most_common(1)[0][1])

ls = len(s[0])
if n >= ls:
    print('Draw')
    return

def modify(sc, n, ls):
    if sc == ls and n == 1:
        return sc - 1
    else:
        return min(sc + n, ls)
sc = [modify(scx, n, ls) for scx in sc]

m = max(sc)
if sc.count(m) > 1:
    print('Draw')
else:
    print(names[sc.index(m)])
