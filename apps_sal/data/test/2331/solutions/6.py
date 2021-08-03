from math import gcd

t = int(input())

for _ in range(t):
    a, b = list(map(int, input().split()))
    if gcd(a, b) == 1:
        print("Finite")
    else:
        print("Infinite")
