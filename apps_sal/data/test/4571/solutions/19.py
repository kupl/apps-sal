n, m = map(int, input().split())
e = 2**m
print((1900 * m + 100 * (n - m)) * e)
