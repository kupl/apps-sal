"""input
3 5 2
aaa
baaab
1 3
1 1
"""
from bisect import bisect_left, bisect_right
(n, m, q) = list(map(int, input().split()))
(s, t) = (input(), input())
x = []
for i in range(len(s) - len(t) + 1):
    if s[i:i + len(t)] == t:
        x.append(i)
sx = set(x)
for _ in range(q):
    (l, r) = list(map(int, input().split()))
    if r - l + 1 < len(t):
        print(0)
        continue
    i = bisect_right(x, l - 1)
    j = bisect_left(x, r - len(t))
    if l - 1 in sx:
        i -= 1
    if r - len(t) not in sx:
        j -= 1
    print(j - i + 1)
