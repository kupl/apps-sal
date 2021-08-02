import math
A, B, C = map(int, open(0).readline().split())
print('YES' if C % math.gcd(B, A % B) == 0 else 'NO')
