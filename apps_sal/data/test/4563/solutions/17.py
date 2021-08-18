import math
from fractions import Fraction
n = int(input())
anst = 1
ansa = 1
for _ in range(n):
    ti, ai = list(map(int, input().split()))
    anst = ti * math.ceil(max(Fraction(anst, ti), Fraction(ansa, ai)))
    ansa = ai * math.ceil(max(Fraction(anst, ti), Fraction(ansa, ai)))

print((int(anst + ansa)))
