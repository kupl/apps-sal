import math
import sys
input = sys.stdin.readline


t = int(input())

for test in range(t):
    a, b = list(map(int, input().split()))
    k = math.gcd(a, b)

    if k != 1:
        print("Infinite")
    else:
        print("Finite")
