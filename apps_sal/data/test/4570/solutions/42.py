import sys
sys.setrecursionlimit(10 ** 6)
(n, a, b) = list(map(int, input().split()))
print(min(b, n * a))
