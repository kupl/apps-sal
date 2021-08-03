import math
from functools import reduce

N, X = list(map(int, input().split()))
x = list(map(int, input().split()))
x.append(X)
x.sort()
ans = x[1] - x[0]
for i in range(1, N):
    ans = math.gcd(ans, x[i + 1] - x[i])

print(ans)
