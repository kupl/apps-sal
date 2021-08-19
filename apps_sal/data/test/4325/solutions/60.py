import math
(N, X, T) = map(int, input().split())
print(T * math.ceil(N / X))
