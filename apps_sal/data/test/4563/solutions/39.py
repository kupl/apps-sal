import math
from fractions import Fraction

N = int(input())
a, b = map(int, input().split())
ret_a = a
ret_b = b
for _ in range(1, N):
    a, b = map(int, input().split())
    x = math.ceil(max(Fraction(ret_a, a), Fraction(ret_b, b)))
    ret_a = a * x
    ret_b = b * x
print(ret_a + ret_b)
