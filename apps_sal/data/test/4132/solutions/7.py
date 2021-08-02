import math
N = int(input())
A = list(map(int, input().split()))
x = A[0]
for a in A:
    x = math.gcd(x, a)
print(x)
