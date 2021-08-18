import sys
from collections import defaultdict

input = sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
acc = [0 for _ in range(N + 1)]
mod_count = defaultdict(int)
mod_count[0] += 1

for i, a_i in enumerate(A):
    acc[i + 1] = acc[i] + a_i
    mod = acc[i + 1] % M
    ans += mod_count[mod]
    mod_count[mod] += 1

print(ans)
