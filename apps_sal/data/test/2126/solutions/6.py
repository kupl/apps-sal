from sys import stdin, stdout
(n, m, h) = map(int, input().split())
front = list(map(int, input().split()))
side = list(map(int, input().split()))
top = [None] * n
for i in range(n):
    top[i] = list(map(int, input().split()))
    for j in range(m):
        if top[i][j] == 1:
            top[i][j] = min(front[j], side[i])
for i in range(n):
    for j in top[i]:
        print(j, end=' ')
    print('')
