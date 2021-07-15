from fractions import Fraction
n=int(input())
a=[int(i) for i in input().split()]
a=sorted(a)
s=[]
s.append(0)
for i in range(n):
    s.append(s[-1]+a[i])
ans=0
for i in range(1,n+1):
    ans+=s[n]-s[i-1]-(n-i+1)*a[i-1]
ans=ans*2+sum(a)
ans=Fraction(ans,n)
print("{0:d} {1:d}".format(ans.numerator,ans.denominator))

