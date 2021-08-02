import numpy as np
n, k = list(map(int, input().split()))
a = np.array(input().split(), dtype=int)
n1 = [0 for i in range(40)]
g0 = [0 for i in range(40)]
g1 = [0 for i in range(40)]
ss = [0 for i in range(40)]
t2 = [1 for i in range(40)]

for i in range(40):
    n1[i] = np.count_nonzero(a & 1)
    a >>= 1
    if i > 0:
        t2[i] = t2[i - 1] * 2
    g0[i] = n1[i] * t2[i]
    g1[i] = (n - n1[i]) * t2[i]
    if n1[i] < n - n1[i]:
        ss[i] = ss[i - 1] + g1[i]
    else:
        ss[i] = ss[i - 1] + g0[i]


def DFS(ni, ki, sm):
    if ni == 0:
        if ki == 0:
            return sm + g0[0]
        else:
            return sm + ss[0]
    else:
        if ki // t2[ni] == 0:
            return DFS(ni - 1, ki, sm + g0[ni])
        elif ki // t2[ni] > 1:
            return sm + ss[ni]
        else:
            return max(sm + g0[ni] + ss[ni - 1], DFS(ni - 1, ki - t2[ni], sm + g1[ni]))


ma = DFS(39, k, 0)
print(ma)
