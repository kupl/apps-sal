from functools import reduce
def R(): return map(int, input().split())
def F(x, y): return (x[0] + 1, y[1]) if x[1] + y[1] > m else (x[0], x[1] + y[1])


n, m = R()
s = reduce(F, zip([0] * n, R()), (1, 0))
print(s[0])
