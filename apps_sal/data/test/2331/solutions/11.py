import math

n, = list(map(int, input().split()))
for _ in range(n):
    a, b = list(map(int, input().split()))
    if math.gcd(a, b) == 1:
        print("Finite")
    else:
        print("Infinite")

