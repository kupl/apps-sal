from fractions import Fraction
def __starting_point():
    p,q=list(map(int, input().split(' ')))
    n=int(input())
    a=list(map(int,input().split(' ')))
    def fract(x):
        if x==n-1:
            return Fraction(1,a[x])
        elif x>=n:
            return 0
        else:
            return Fraction(1,a[x]+fract(x+1))
    print('YES' if Fraction(p,q)==a[0]+fract(1) else 'NO')





__starting_point()
