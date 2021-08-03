import math
A, B = [int(n) for n in input().split()]

print((int(A * B / math.gcd(A, B))))
