n, m = map(int, input().split())
a = 0
while m:
    a += n // m
    n, m = m, n % m
print(a)
