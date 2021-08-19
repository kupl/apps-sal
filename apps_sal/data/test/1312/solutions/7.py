(n, m) = map(int, input().split())
for i in range(0, m):
    print(n // m + (i < n % m), end=' ')
