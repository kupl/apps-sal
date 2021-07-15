from functools import reduce
n, m = map(int, input().split())
a = list(zip([0] * n, map(int, input().split())))
s = reduce(lambda x, y: (x[0] + 1, y[1]) if x[1] + y[1] > m else (x[0], x[1] + y[1]), a, (1, 0))
print(s[0])
