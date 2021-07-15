import numpy as np

N = int(input())
xl = [int(x) for x in input().split()]

xlsorted = np.sort(xl)
m1 = xlsorted[int(N/2)-1]
m2 = xlsorted[int(N/2)]

for i in range(N):
    if xl[i] <= m1:
        print(m2)
    else:
        print(m1)

