(n, k) = map(int, input().split())
d = n // (2 * (k + 1))
g = k * d
r = n - d - g
print(str(d) + ' ' + str(g) + ' ' + str(r))
