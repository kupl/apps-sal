import sys
input = sys.stdin.readline
b = int(input())
g = int(input())
n = int(input())
print(n + 1 - max(n - b, 0) - max(n - g, 0))
