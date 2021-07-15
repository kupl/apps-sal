import sys
import math

input = sys.stdin.readline
N, X = map(int, input().split())
A = list(map(int, input().split()))

gcd = abs(X - A[0])
for a_i in A:
    gcd = math.gcd(gcd, abs(X-a_i))

print(gcd)
