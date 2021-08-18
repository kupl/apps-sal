from math import gcd
from collections import defaultdict
mod = 10**9 + 7
n = int(input())
mp = defaultdict(lambda: [0, 0])
zero_zero = 0
for i in range(n):
    a, b = list(map(int, input().split()))
    if a == 0 and b == 0:
        zero_zero += 1
        continue
    g = gcd(a, b)
    a //= g
    b //= g
    rot_cnt = 0
    while not (a > 0 and b >= 0):
        a, b = -b, a
        rot_cnt += 1
    mp[(a, b)][rot_cnt % 2] += 1
ans = 1
for s, t in list(mp.values()):
    now = (pow(2, s, mod) + pow(2, t, mod) - 1) % mod
    ans = (ans * now) % mod
ans = (ans - 1 + zero_zero) % mod
print(ans)
