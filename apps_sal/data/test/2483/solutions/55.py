import numpy as np
(N, C) = map(int, input().split())
T1 = [[] for _ in range(C)]
for _ in range(N):
    (s, t, c) = map(int, input().split())
    T1[c - 1].append([s, t])
for i in range(C):
    T1[i].sort()
T2 = [[] for _ in range(C)]
for i in range(C):
    for (s, t) in T1[i]:
        if len(T2[i]) != 0 and T2[i][-1][1] == s:
            T2[i][-1][1] = t
        else:
            T2[i].append([s, t])
L = np.zeros(10 ** 5 + 2, int)
for i in range(C):
    for time in T2[i]:
        L[time[0]] += 1
        L[time[1] + 1] -= 1
ans = L.cumsum().max()
print(ans)
