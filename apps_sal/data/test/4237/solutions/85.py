import math

a, b, c, d = map(int, input().split())
l = c * d // math.gcd(c, d)
all = b - a + 1
can_c = b // c - (a - 1) // c
can_d = b // d - (a - 1) // d
can_cd = b // l - (a - 1) // l
ans = all - can_c - can_d + can_cd
print(ans)
