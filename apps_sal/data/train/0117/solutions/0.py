from sys import stdin
input = stdin.readline
tests = int(input())
for test in range(tests):
    (n, m) = list(map(int, input().split()))
    a = [[0] * m for _ in range(n)]
    r = [[int(i) for i in input().split()] for _ in range(n)]
    c = [[int(i) for i in input().split()] for _ in range(m)]
    z = [[-1, -1] for _ in range(n * m + 1)]
    for i in range(n):
        for j in range(m):
            z[r[i][j]][0] = j
    for i in range(m):
        for j in range(n):
            z[c[i][j]][1] = j
    for i in range(1, n * m + 1):
        a[z[i][1]][z[i][0]] = i
    for i in a:
        print(' '.join([str(j) for j in i]))
