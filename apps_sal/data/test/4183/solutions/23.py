import math
N = int(input())
T = int(input())
for i in range(N - 1):
    t = int(input())
    T = T // math.gcd(T, t) * t
print(T)
