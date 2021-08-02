import sys
3
input = lambda: sys.stdin.readline().strip()
n = int(input())
odd = sum(1 for i in range(1, n + 1, 2))
even = sum(1 for i in range(2, n + 1, 2))
print((odd / (odd + even)))
