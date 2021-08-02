import numpy as np

N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]

AB_sort = sorted(AB, key=lambda x: x[1])

A = [x[0] for x in AB_sort]
B = [x[1] for x in AB_sort]

A_cum = np.array(A).cumsum()

for i in range(N):
    if A_cum[i] > B[i]:
        print('No')
        return

print('Yes')
