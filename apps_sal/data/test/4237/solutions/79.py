import math
a, b, c, d = list(map(int, input().split()))

GCD = math.gcd(c, d)
LCM = c*d//GCD
print((b-b//c-b//d+b//LCM-a+1+(a-1)//c+(a-1)//d-(a-1)//LCM))

