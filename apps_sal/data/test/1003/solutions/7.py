(n, m) = list(map(int, input().split()))
r = 0
while n >= m:
    r += m
    n -= m - 1
print(r + n)
