from math import *
(A, B, N) = map(int, input().split())
print(floor(A * min(N, B - 1) / B))
