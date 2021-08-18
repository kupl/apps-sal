import math

N = int(input())
csf = [list(map(int, input().split())) for _ in range(N - 1)]


for i in range(N):
    t = 0
    for j in range(i, N - 1):
        if csf[j][1] >= t:
            t = csf[j][1] + csf[j][0]
        else:
            t = csf[j][1] + math.ceil((t - csf[j][1]) / csf[j][2]) * csf[j][2] + csf[j][0]
    print(t)
