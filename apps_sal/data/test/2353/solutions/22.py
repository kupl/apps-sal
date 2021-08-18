import math
T = int(input())
n = [0] * T
m = [0] * T
a = [0] * T
p = [0] * T


for t in range(T):
    a, b, c, d = [int(i) for i in input().split(' ')]
    if b >= a:
        print(b)
    elif c <= d:
        print(-1)
    else:
        print(b + (math.ceil((a - b) / (c - d))) * c)
