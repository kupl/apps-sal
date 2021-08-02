from bisect import bisect_left
from itertools import product
from sys import maxsize

a, b, q = list(map(int, input().split()))
s = [-maxsize] + [int(input()) for _ in range(a)] + [maxsize]
t = [-maxsize] + [int(input()) for _ in range(b)] + [maxsize]

for _ in range(q):
    x = int(input())
    i = bisect_left(s, x)
    j = bisect_left(t, x)
    res = maxsize
    for ss, tt in product((s[i - 1], s[i]), (t[j - 1], t[j])):
        res = min(res, abs(ss - x) + abs(tt - ss), abs(tt - x) + abs(ss - tt))
    print(res)
