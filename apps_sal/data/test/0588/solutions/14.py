from itertools import combinations
from cmath import phase
N = int(input())
XY = [complex(*list(map(int, input().split()))) for _ in range(N)]
XY.sort(key=phase)
XY += XY
print((max(abs(sum(XY[i:j])) for i, j in combinations(list(range(N*2+1)), 2) if j-i<=N)))

