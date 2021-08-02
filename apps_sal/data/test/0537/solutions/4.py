n, k = list(map(int, input().split()))
a = n // (2 * (k + 1))
b = k * a
c = n - a - b
print(a, b, c)
