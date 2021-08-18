from fractions import Fraction

n = int(input())
l = [int(x) for x in input().split()]
l.sort()

f = Fraction(sum([(3 - 2 * n + 4 * i) * l[i] for i in range(n)]), n)
print(f.numerator, f.denominator)
