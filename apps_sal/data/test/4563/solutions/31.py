import math
from fractions import Fraction
from decimal import *
# ex) Fraction(2,6) > 1/3 > 0.33333

n = int(input())
x, y = list(map(int, input().split()))
t, a = x, y

for _ in range(n - 1):
    tt, aa = list(map(int, input().split()))

    # c = 1
    '''
    if (t >= a):
        c = math.ceil(tt / t)

    else:
        c = math.ceil(aa / a)
    '''
    # c = math.ceil(max(t / tt, a / aa))
    # c = math.ceil(max(Fraction(t + tt - 1, tt), Fraction(a + aa - 1 / aa)))
    c = max(math.ceil(Fraction(t, tt)), math.ceil(Fraction(a, aa)))
    c = max(1, c)

    t = tt * c
    a = aa * c


ans = t + a
print(ans)
