import numpy as np
N = int(input())
xy = [list(map(int, input().split(" "))) for i in range(N)]

L = 0
for i in range(N):
    for j in range(N):
        a = xy[i][0] - xy[j][0]
        b = xy[i][1] - xy[j][1]
        l = np.sqrt(a**2 + b**2)
        L += l

print((L / N))
