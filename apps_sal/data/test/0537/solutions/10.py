n, k = list(map(int, input().split()))
d = int(n // (2 * k + 2))
c = k * d
s = n - c - d
print(d, c, s)
