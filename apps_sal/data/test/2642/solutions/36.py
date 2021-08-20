from collections import defaultdict, deque
import math
kMod = 1000000007
N = int(input())
key2count = defaultdict(lambda: [0, 0])
for _ in range(N):
    (a, b) = map(int, input().split())
    g = math.gcd(a, b)
    if a < 0 or (a == 0 and b < 0):
        (a, b) = (-a, -b)
    if g > 0:
        (a, b) = (a // g, b // g)
    idx = 0
    if b <= 0:
        idx = 1
        (a, b) = (-b, a)
    key2count[a, b][idx] += 1
ans = 1
for (key, val) in key2count.items():
    if key == (0, 0):
        continue
    (plus, minus) = val
    ans *= pow(2, plus, kMod) + pow(2, minus, kMod) - 1
    ans %= kMod
ans += sum(key2count[0, 0])
print((ans + kMod - 1) % kMod)
