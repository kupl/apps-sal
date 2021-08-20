(n, m) = map(int, input().split())
for i in range(0, m):
    print(n // m + (n % m != 0 and i < n % m), end=' ')
