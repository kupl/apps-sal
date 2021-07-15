import math
N = int(input())
A = list(map(int, input().split()))
ans = 0
for i in range(N):
    ans = math.gcd(ans, A[i])

print(ans)
