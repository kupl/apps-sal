import sys
import math
(N, M) = map(int, sys.stdin.readline().split())
ans = 0
for i in range(1, int(M ** 0.5) + 1):
    if M % i == 0:
        j = M // i
        r1 = j // N
        r2 = j % N
        ans = max(ans, min(r1, math.gcd(r1, r2)) * i)
        r1 = i // N
        r2 = i % N
        ans = max(ans, min(r1, math.gcd(r1, r2)) * j)
print(ans)
