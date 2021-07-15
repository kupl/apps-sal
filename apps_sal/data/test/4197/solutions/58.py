3
import sys
input = lambda: sys.stdin.readline().strip()
n = int(input())
a = [int(x) for x in input().split()]
print((*(x + 1 for x in sorted(list(range(n)), key=lambda i: a[i]))))

