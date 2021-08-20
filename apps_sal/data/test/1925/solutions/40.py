import math
(A, B, N) = list(map(int, input().split()))
x = min(B - 1, N)
print(math.floor(A * x / B))
