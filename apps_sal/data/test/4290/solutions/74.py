from math import floor
n, m = list(map(int, input().split()))
a = (n * (n - 1)) / 2
b = (m * (m - 1)) / 2
print((floor(a + b)))
