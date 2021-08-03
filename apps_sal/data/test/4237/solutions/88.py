import math
A, B, C, D = map(int, input().split())

LCD = C * D // math.gcd(C, D)

ans = B - (B // C + B // D - B // LCD) - ((A - 1) - ((A - 1) // C + (A - 1) // D - (A - 1) // LCD))

print(int(ans))
