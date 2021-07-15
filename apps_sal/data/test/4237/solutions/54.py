import math
A, B, C, D = map(int, input().split(' '))
CD_least_common = C * D // math.gcd(C, D)
except_rst = B // C - (A - 1) // C + B // D - (A - 1) // D - (B // CD_least_common - (A - 1) // CD_least_common)
rst = B - (A - 1) - except_rst
print(rst)
