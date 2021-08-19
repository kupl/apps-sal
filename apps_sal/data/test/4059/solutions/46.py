import math
N = int(input())
S = 0
for A in range(1, N):
    S += max(0, int(math.ceil(N / A) - 1))
print(S)
