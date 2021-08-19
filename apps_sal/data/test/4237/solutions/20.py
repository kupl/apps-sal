import math
(A, B, C, D) = map(int, input().split())
E = C * D // math.gcd(C, D)
A -= 1
print(B - A - (B // C - A // C) - (B // D - A // D) + (B // E - A // E))
