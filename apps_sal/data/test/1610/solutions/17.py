(n, k) = (int(x) for x in input().split())
for i in range(n, n - k, -1):
    print(i, end=' ')
for i in range(1, n - k + 1):
    print(i, end=' ')
