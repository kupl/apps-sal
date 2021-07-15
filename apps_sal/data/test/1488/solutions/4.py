from fractions import Fraction
while(1):
    try:
        n=int(input())
        a=list(map(int,input().split()))
        s=sum(a)
        a.sort()
        for i in range(0,n):
            s+=2*(2*i+1-n)*a[i]
        f=Fraction(s,n)
        print(f.numerator,end=' ')
        print(f.denominator)
    except EOFError:
        break
