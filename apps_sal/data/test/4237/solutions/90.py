import math
[A, B, C, D] = [int(i) for i in input().split()]
u = int(C * D / math.gcd(C, D))
s = B // C - A // C + B // D - A // D - B // u + A // u + 1
t = 0
if A % C != 0:
    t -= 1
if A % D != 0:
    t -= 1
if A % u != 0:
    t += 1
s += t
ans = B - A + 1 - s
print(ans)
