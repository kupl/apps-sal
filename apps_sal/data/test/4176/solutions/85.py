import math
A, B = map(int, input().split())
a = math.gcd(A, B)
ans = A * B // a
print(ans)
