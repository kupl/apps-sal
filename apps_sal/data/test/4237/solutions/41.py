from math import gcd
a, b, c, d = map(int, input().split())
lcm = c*d // gcd(c, d)
ans = b - (b//c + b//d - b//lcm) - (a-1 - ((a-1)//c + (a-1)//d - (a-1)//lcm))
print(ans)
