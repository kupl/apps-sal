import sys
t = 1
t = int(input())
for i in range(t):
    n, m = list(map(int, sys.stdin.readline().strip().split()))
    x = n // m
    n
    print(x * m + min(n - x * m, m // 2))
