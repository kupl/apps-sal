import math as mt
import itertools as it
import functools as ft
stdin = lambda type_='int', sep=' ': list(map(eval(type_), input().split(sep)))
joint = lambda sep=' ', *args: sep.join((str(i) if type(i) != list else sep.join(map(str, i)) for i in args))
n = int(input())
a = stdin()
ans = 10 ** 6 - a[0]
for i in range(n):
    ans = min(ans, max(a[i] - 1, 10 ** 6 - (a[i + 1] if i != n - 1 else 10 ** 6)))
print(ans)
