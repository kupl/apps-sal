n, k = map(int, input().split())
for i in list(range(n, n - k, -1)) + list(range(1, n - k + 1)):
    print(i, end=' ')
