n, k = [int(i) for i in input().split()]
a = [[0] * n for i in range(n)]
for i in range(n):
    a[i][i] = k
for i in a:
    print(*i)
