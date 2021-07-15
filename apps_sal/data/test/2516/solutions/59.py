3
import sys
from collections import Counter
input = lambda: sys.stdin.readline().strip()
n, p = [int(x) for x in input().split()]
s = input()
ans = 0
if p == 2 or p == 5:
    allowed_digits = '24680' if p == 2 else '50'
    for i, c in enumerate(s, start=1):
        if c in allowed_digits:
            ans += i
else:
    def minv(x, p):
        return pow(x, p - 2, p)

    count = Counter({0: 1})
    x, delta = 0, 1
    for c in s:
        x = ((x * 10) + ord(c) - ord('0')) % p
        y = (x * minv(delta, p)) % p
        ans += count[y]
        count[y] += 1
        delta = (delta * 10) % p

print(ans)

