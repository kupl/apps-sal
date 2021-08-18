
from collections import Counter
import sys
readline = sys.stdin.readline

N, M = map(int, readline().split())
A = [0] + list(map(int, readline().split()))

for i in range(1, len(A)):
    A[i] = A[i - 1] + A[i]

A = list(map(lambda x: x % M, A))

c = Counter(A)

ans = 0
for v in c.values():
    ans += (v * (v - 1)) // 2

print(ans)
