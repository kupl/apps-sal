(n, k) = map(int, input().split())
for i in range(k + 1, 0, -1):
    print(i, end=' ')
for i in range(k + 2, n + 1):
    print(i, end=' ')
