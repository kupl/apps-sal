import sys
3
input = lambda: sys.stdin.readline().strip()
p, q, r = [int(x) for x in input().split()]
print(min(p + q, q + r, r + p))
