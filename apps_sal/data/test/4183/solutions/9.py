import math
N = int(input())
a = [int(input()) for _ in range(N)]
ans = a[0]
for i in range(1, N):
    ans = ans * a[i] // math.gcd(ans, a[i])
print(ans)
