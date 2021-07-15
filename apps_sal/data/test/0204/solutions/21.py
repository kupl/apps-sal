from fractions import gcd
a,b,x,y = list(map(int,input().split()))

gcd_val = gcd(x, y)
x //= gcd_val
y //= gcd_val

print(min(a//x,b//y))

