"""
Created on Aug 26, 2016

@author: Md. Rezwanul Haque
"""
'\nF = []\na,b = 0,1\n#F.append(a)\nfor _ in range(5):\n    F.append(b)\n    a,b = b,a+b\nprint(F)\n'


def go(a, b):
    (res, c) = (0, a + b)
    if d.get(c) and d[c] > 0:
        d[c] -= 1
        res = go(b, c) + 1
        d[c] += 1
    return res


input()
d = {}
for i in map(int, input().split()):
    if d.get(i):
        d[i] += 1
    else:
        d[i] = 1
ans = 2
for a in d:
    for b in d:
        if a != b or d[a] > 1:
            d[a] -= 1
            d[b] -= 1
            cnt = go(a, b) + 2
            d[a] += 1
            d[b] += 1
            ans = max(ans, cnt)
print(ans)
