from sys import stdin

(n, l, r) = (int(i) for i in stdin.readline().split())

m = 2 ** l - 1 + n - l
M = 2 ** r - 1 + (2 ** (r - 1) * (n - r))

print(m, M)
