from functools import reduce
R = lambda: map(int, input().split())
F = lambda x, y: (x[0] + 1, y[1]) if x[1] + y[1] > m else (x[0], x[1] + y[1])
n, m = R()
s = reduce(F, zip([0] * n, R()), (1, 0))
print(s[0])
