import sys
import math


def f(x: int, y: int) -> int:
    return max(len(str(x)), len(str(y)))


n = int(input())
min_f_value = sys.maxsize

for a in range(1, int(math.sqrt(n)) + 1):
    b, rem = divmod(n, a)
    if rem == 0:
        min_f_value = min(min_f_value, f(a, b))

print(min_f_value)
