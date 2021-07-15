from fractions import Fraction 
x,y,n=map(int,input().split())
ans=Fraction(x,y).limit_denominator(n)
num=ans.numerator
denom=ans.denominator
print (str(num) + '/' + str(denom))
