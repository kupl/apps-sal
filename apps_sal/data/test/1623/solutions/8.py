n, l, r = map(int, input().split())
a = (n - l) + (2 ** l - 1)
b = (n - r) * (2 ** (r - 1)) + (2 ** r - 1)
print(a, b)
