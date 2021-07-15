t = int(input())
for case in range(t):
    n, m = [int(x) for x in input().split(' ')]
    a = [[int(x) for x in input().split(' ')] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if (a[i][j] - (i + j)) % 2 != 0:
                a[i][j] += 1
    for row in a:
        print(*row)


