import math
import functools as ft
import itertools as it

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b.sort()
q = b[-1] + b[-2]
print('YES' if sum(a) <= q else 'NO')
