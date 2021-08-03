import math

N = int(input())

res = 0
for a in range(1, N):
    res += math.floor((N - 1) / a)

print(res)
