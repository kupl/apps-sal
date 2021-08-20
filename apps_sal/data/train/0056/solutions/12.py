import math
import sys
input = sys.stdin.readline
T = int(input())


def f(M):
    minR = math.inf
    maxR = -math.inf
    minC = math.inf
    maxC = -math.inf
    for i in range(len(M)):
        sumRow = sum(M[i])
        minR = min(minR, sumRow)
        maxR = max(maxR, sumRow)
        sumCol = sum([M[el][i] for el in range(len(M))])
        maxC = max(maxC, sumCol)
        minC = min(minC, sumCol)
    return (maxR - minR) ** 2 + (maxC - minC) ** 2


for t in range(T):
    (N, K) = [int(_) for _ in input().split()]
    M = [[0] * N for i in range(N)]
    for i in range(K):
        M[i % N][(i // N + i) % N] = 1
    print(f(M))
    for row in M:
        print(''.join(map(str, row)))
