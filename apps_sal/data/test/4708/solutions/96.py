from sys import stdin
input = stdin.readline

n, k, x, y = list(map(int, stdin.read().split()))

print((min(k, n) * x + max(0, n - k) * y))
