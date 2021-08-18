from collections import deque

N = int(input())
F = []
for i in range(N):
    F.append([int(x) for x in input().split()])

P = []
for i in range(N):
    P.append([int(x) for x in input().split()])

ret = None
for bit in range(1, 2**10):
    nWork = [0] * N
    for i in range(10):
        if (bit >> i) & 1:
            for shop in range(N):
                if F[shop][i] == 1:
                    nWork[shop] += 1

    cand = 0
    for i in range(N):
        cand += P[i][nWork[i]]
    if ret == None or cand > ret:
        ret = cand
print(ret)
