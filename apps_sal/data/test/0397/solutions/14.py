import sys
import math

n, k = list(map(int, sys.stdin.readline().strip().split()))
a = (2 * n + 3 - math.sqrt((2*n+3)**2 - 4 * (n**2 + n - 2 * k))) // 2
print(int(a))
