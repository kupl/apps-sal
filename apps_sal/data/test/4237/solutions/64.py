import math

a, b, c, d = map(int, input().split())

def f(x, y):
    return (x*y//math.gcd(x, y))

z = f(c, d)
print(b - a + 1 - ((b//c - (a-1)//c) + (b//d - (a-1)//d) - (b//z - (a-1)//z)))
