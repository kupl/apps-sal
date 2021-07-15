
n, l, r = list(map(int, input().split(' ')))

mnres = 0
mxres = 0

mnres = 2 ** l - 1 + (n - l)
mxres = 2 ** r - 1 + (n - r) * (2 ** (r - 1))

print(mnres, mxres)

