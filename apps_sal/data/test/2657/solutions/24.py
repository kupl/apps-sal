import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

n = max(A)
mid = n / 2
r = float("inf")
for a in A:
    if a == n:
        continue
    if abs(mid - r) > abs(mid - a):
        r = a

print(n, r)
