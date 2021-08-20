import sys
input = sys.stdin.readline
mex = [[1, 2, 1], [2, 0, 0], [1, 0, 0]]
N = int(input())
a = [list(map(int, input().split()))]
for i in range(1, N):
    a.append([int(input())])
    if i < 4:
        stop = N
    else:
        stop = min(4, N)
    for j in range(1, stop):
        a[i].append(mex[a[i - 1][j]][a[i][j - 1]])
count = [0, 0, 0]
for (i, ai) in enumerate(a):
    for (j, aij) in enumerate(ai):
        if i >= 3 and j >= 3:
            count[aij] += N - max(i, j)
        else:
            count[aij] += 1
print(*count)
