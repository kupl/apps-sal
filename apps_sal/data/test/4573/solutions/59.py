import math
import statistics
n = int(input())
xL = list(map(int, input().split(' ')))
xL2 = []
for i in range(n):
    xL2.append([i, xL[i]])
xL2 = sorted(xL2, key=lambda x: x[1])
if n % 2 == 0:
    center = n // 2
    centers = [xL2[center - 1], xL2[center]]
    for i in range(n):
        if i == centers[0][0] or i == centers[1][0]:
            print(statistics.median(xL[:i] + xL[i + 1:]))
        elif centers[0][1] < xL[i]:
            print(centers[0][1])
        else:
            print(centers[1][1])
else:
    center = n // 2
    centers = [xL2[center - 1], xL2[center], xL2[center + 1]]
    for i in range(n):
        if i == centers[0][0] or i == centers[1][0] or i == centers[2][0]:
            print(statistics.median(xL[:i] + xL[i + 1:]))
        elif centers[0][1] < xL[i]:
            print((centers[0][1] + centers[1][1]) / 2)
        else:
            print((centers[1][1] + centers[2][1]) / 2)
