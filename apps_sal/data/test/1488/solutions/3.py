from fractions import Fraction

n = int(input())
l = [int(x) for x in input().split()]
l.sort()

f = Fraction(sum([(3-2*n+4*i)*l[i] for i in range(n)]),n)
print(f.numerator,f.denominator)

##import itertools
##tot2 = 0
##for i in itertools.permutations(l):
##    loc = 0
##    tot = 0
##    for e in i:
##        tot += abs(loc-e)
##        loc = e
##    #print(i,tot)
##    tot2 += tot
##import math
##f2 = Fraction(tot2,math.factorial(n))
##print(f2.numerator,f2.denominator)
##

