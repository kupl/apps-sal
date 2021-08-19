import math
(N, X, T) = map(int, input().split())
t_times = N / X
result = T * math.ceil(t_times)
print(result)
