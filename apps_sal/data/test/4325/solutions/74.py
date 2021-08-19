import math
(N, X, T) = list(map(int, input().split()))
print(T * math.ceil(N / X))
