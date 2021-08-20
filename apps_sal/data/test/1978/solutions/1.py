import sys
import copy
input = sys.stdin.readline
n = int(input())
EDGE = [list(map(int, list(input().strip()))) for i in range(n)]
m = int(input())
P = list(map(int, input().split()))
Distance = copy.deepcopy(EDGE)
for i in range(n):
    for j in range(n):
        if Distance[i][j] == 0 and i != j:
            Distance[i][j] = float('inf')
for k in range(n):
    for i in range(n):
        for j in range(n):
            length = Distance[i][k] + Distance[k][j]
            if Distance[i][j] > length:
                Distance[i][j] = length
ANS = [P[0]]
NOW = 0
i = 1
while i < m:
    if Distance[P[NOW] - 1][P[i] - 1] == i - NOW:
        i += 1
    else:
        ANS.append(P[i - 1])
        NOW = i - 1
ANS.append(P[-1])
print(len(ANS))
print(*ANS)
