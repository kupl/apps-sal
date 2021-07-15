from fractions import *
n  =  int(input())

a = [int(x) for x in input().split()]
a.sort()
a1 = a[0]
lef_sum = 0
for i in range(1,n):
    lef_sum+= a[i]*i - a1 
    a1+=a[i]
    
lef_sum*=2
total = lef_sum+a1
s = Fraction(total,n)
print(s.numerator,s.denominator)


