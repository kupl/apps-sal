import math
[A, B] = [int(i) for i in input().split()]
ans = A*B/math.gcd(A, B)
print(int(ans))
