import sys
3
def input(): return sys.stdin.readline().strip()


p, q, r = [int(x) for x in input().split()]
print(min(p + q, q + r, r + p))
