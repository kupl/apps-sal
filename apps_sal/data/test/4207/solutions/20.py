from fractions import Fraction
import collections
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []
abzero = 0
bzero = 0
for i in range(n):
    if a[i] == 0:
        if b[i] == 0:
            abzero += 1
    elif b[i] == 0:
        bzero += 1
    else:
        c.append(Fraction(a[i], b[i]).limit_denominator(1000000000))
c = collections.Counter(c)
try:
    ma = c.most_common()[0][1]
except IndexError:
    ma = 0
print(max(ma + abzero, abzero + bzero))
