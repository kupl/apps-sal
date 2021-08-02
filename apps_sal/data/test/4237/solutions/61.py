import math
A, B, C, D = map(int, input().split())
if A % C == 0:
    divC = B // C - A // C + 1
else:
    divC = B // C - A // C
if A % D == 0:
    divD = B // D - A // D + 1
else:
    divD = B // D - A // D
lcm = C * D // math.gcd(C, D)
if A % lcm == 0:
    divlcm = B // lcm - A // lcm + 1
else:
    divlcm = B // lcm - A // lcm
print(B - A + 1 - divC - divD + divlcm)
