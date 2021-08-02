import math
a, b, c, d = map(int, input().split())
p = c * d // math.gcd(c, d)
x = b // c + b // d - b // p - ((a - 1) // c + (a - 1) // d - (a - 1) // p)
ans = b - a + 1 - x
print(ans)
