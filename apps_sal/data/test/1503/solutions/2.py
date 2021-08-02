import sys
input = sys.stdin.readline

n, m = list(map(int, sys.stdin.readline().split()))

A = [list(map(int, sys.stdin.readline().split())) for i in range(m)]

LISTS = [[None for i in range(n + 1)] for i in range(m)]

for i in range(n):
    for j in range(m):
        LISTS[j][A[j][i]] = i

ANS = 0
i = 0
while i < n:
    x = A[0][i]

    check = 1
    # print(ANS,i)
    for j in range(i + 1, n + 1):
        for k in range(1, m):
            if LISTS[k][x] + (j - i) < n and j < n and A[k][LISTS[k][x] + (j - i)] == A[0][j]:
                continue
            else:
                check = 0
                break

        if check == 0:
            break

    ANS += (j - i) * (j - i + 1) // 2
    i = j


print(ANS)
