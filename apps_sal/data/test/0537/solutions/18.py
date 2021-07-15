n, k = map(int, input().split())
# d * (k + 1) * 2 <= n
d = n // (2 * (k + 1))
g = k * d
r = n - d - g
print(str(d) + " " + str(g) + " " + str(r))
