from math import ceil
(n, m) = list(map(int, input().split()))
base = (n - m) * 100 + 1900 * m
allok = pow(2, m)
'\n1回目はbase秒かかる\n2回目の期待値は、1回目の時点から考えるとbase + (allok-1)*y\n'
print(base * allok)
