
from collections import deque
L = int(input())

Lbin = (bin(L)[2:])[::-1]
N = len(Lbin)
M = 0
E = deque()

for i in range(0, N - 1):
    E.append(((i + 1, i + 2), 0))
    E.append(((i + 1, i + 2), 2 ** i))
    M += 2

weight = L
for i in range(0, N - 1):
    if Lbin[i] == '1':  # 2^iの位
        weight -= 2 ** i
        E.append(((i + 1, N), weight))
        M += 1

print((N, M))
for e in E:
    print((e[0][0], e[0][1], e[1]))
