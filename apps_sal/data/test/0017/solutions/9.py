import sys

n, k, t = [int(d) for d in sys.stdin.readline().split()]
if t < k:
    print(t)
elif t > n:
    print(n+k-t)
else:
    print(k)

