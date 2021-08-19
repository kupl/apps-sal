import math
(a, b, x) = map(int, input().split())
a_c = a // x if a % x == 0 else a // x + 1
b_f = b // x
print(b_f - a_c + 1)
