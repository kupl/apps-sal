import math
import sys
input = sys.stdin.readline

t = int(input())


for testcases in range(t):
    r, b, k = list(map(int, input().split()))

    x = math.gcd(r, b)
    r //= x
    b //= x

    if 1 + min(r, b) * (k - 1) < max(r, b):
        print("REBEL")
    else:
        print("OBEY")
