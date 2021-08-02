from sys import stdin, stdout
from collections import deque

n, k = map(int, stdin.readline().split())
n = min(n, k - 1)

l, r = 0, n + 1
while r - l > 1:
    m = (l + r) >> 1

    if k - m <= n:
        r = m
    else:
        l = m

ans = n - r + 1

if not (k & 1) and k // 2 <= n:
    ans -= 1

ans //= 2
stdout.write(str(ans))
