3
import sys
input = lambda: sys.stdin.readline().strip()
n, k = [int(x) for x in input().split()]
h = [int(x) for x in input().split()]
print((sum(1 for x in h if x >= k)))

