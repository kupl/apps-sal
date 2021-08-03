from itertools import *
from numpy import *
n, k = map(int, input().split())
k = 2 * k + 1
s = input()
x = [0] * (s[0] == "0") + [len(list(v))for k, v in groupby(s)] + [0] * (s[-1] == "0")
x1 = array(x[k:])
x2 = array(x[:-k])
x3 = sum(x[:k])
y = [x3] + list(x3 + cumsum(x1 - x2))
print(max(y[::2]))
