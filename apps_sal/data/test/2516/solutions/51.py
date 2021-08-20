from collections import Counter
import sys
3


def input():
    return sys.stdin.readline().strip()


(n, p) = [int(x) for x in input().split()]
s = input()
ans = 0
if p == 2 or p == 5:
    allowed_digits = '24680' if p == 2 else '50'
    for (i, c) in enumerate(s, start=1):
        if c in allowed_digits:
            ans += i
else:
    count = Counter({0: 1})
    (x, e) = (0, 1)
    for c in reversed(s):
        x = (x + (ord(c) - ord('0')) * e) % p
        e = e * 10 % p
        ans += count[x]
        count[x] += 1
print(ans)
