# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
from sys import stdin, stdout
from collections import defaultdict
import math
import copy

#T = int(input())
#N = int(input())
#s = input()
N, M = [int(x) for x in stdin.readline().split()]
#arr = [int(x) for x in stdin.readline().split()]

data = [[0] * M for _ in range(N)]
B = [[0] * M for _ in range(N)]

for i in range(N):
    arr = [int(x) for x in stdin.readline().split()]

    for j in range(M):
        data[i][j] = arr[j]

ans = []

for i in range(N - 1):
    for j in range(M - 1):
        A = data[i][j]
        b = data[i][j + 1]
        c = data[i + 1][j]
        d = data[i + 1][j + 1]

        if A == 1 and b == 1 and c == 1 and d == 1:
            ans.append((i + 1, j + 1))
            B[i][j] = 1
            B[i + 1][j] = 1
            B[i][j + 1] = 1
            B[i + 1][j + 1] = 1

for i in range(N):
    for j in range(M):
        if data[i][j] != B[i][j]:
            print(-1)
            quit()

print(len(ans))
for i in range(len(ans)):
    print(*ans[i])
