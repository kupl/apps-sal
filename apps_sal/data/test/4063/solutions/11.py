import math
N = int(input())
D = sorted(list(map(int, input().split())))
print(D[math.ceil(N / 2)] - D[math.ceil(N / 2) - 1])
