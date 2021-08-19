import math
(N, X) = map(int, input().split())
x = list(map(int, input().split()))
ans = abs(x[0] - X)
for i in range(0, N):
    ans = math.gcd(ans, abs(x[i] - X))
print(ans)
