import math
import itertools


MOD = 1000000007


N = list(map(int, input().split()))[0]
A = list(map(int, input().split()))

l = 1
for i in range(N):
    l = A[i] // math.gcd(A[i], l) * l

# ans = 0
A = [l // x for x in A];
ans = list(itertools.accumulate(A))[-1]
ans %= MOD

# for i in range(N):
#     ans += l // A[i]
#     ans %= MOD

print(ans)

