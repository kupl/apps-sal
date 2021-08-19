import sys
import math
n = [int(i) for i in sys.stdin.read().strip().split('\n')][0]
a = math.ceil(math.sqrt(n))
b = n // a
r = n - a * b
p = 2 * a + 2 * b + (2 if r else 0)
print(p)
