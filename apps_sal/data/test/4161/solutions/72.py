import math

K = int(input())
ans = sum(math.gcd(i, math.gcd(j, k)) for i in range(1, K + 1) for j in range(1, K + 1) for k in range(1, K + 1))
print(ans)
