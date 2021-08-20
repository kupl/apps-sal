(n, m) = map(int, input().split())
max = (n - m + 1) * (n - m) // 2
if m == 1:
    tmp = 0
min = n % m * (n // m * (n // m + 1) // 2) + (m - n % m) * ((n // m - 1) * (n // m) // 2)
print(min, end=' ')
print(max)
