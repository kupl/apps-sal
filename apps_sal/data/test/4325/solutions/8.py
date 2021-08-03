import math
N, X, T = list(map(int, input().split()))

if X >= N:
    print(T)
else:
    print(((math.ceil(N / X)) * T))
