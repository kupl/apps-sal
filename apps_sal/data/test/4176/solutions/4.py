import math
(A, B) = map(int, input().split())
g = math.gcd(A, B)
l = A * B // g
print(l)
