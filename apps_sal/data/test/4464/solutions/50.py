A, B, C = map(int, open(0).readline().split())
import math
print('YES' if C % math.gcd(B,A%B) == 0 else 'NO')
