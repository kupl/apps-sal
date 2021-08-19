from collections import Counter
from fractions import gcd
input()
g, v = Counter(list(map(int, input().split()))), []
while g:
    x = max(g)
    g[x] -= 1
    for y in v:
        g[gcd(x, y)] -= 2
    v.append(x)
    g += Counter()
print(' '.join(map(str, v)))


# Made By Mostafa_Khaled
