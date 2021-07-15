import functools
import operator

x, y = divmod(functools.reduce(operator.add, list(map(int, input().split()))), 5)
print("-1" if y or x == 0 else x)

