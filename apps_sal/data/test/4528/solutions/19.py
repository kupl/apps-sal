import sys
t = 1
t = int(input())
for i in range(t):
    n, m = list(map(int, sys.stdin.readline().strip().split()))
    print((24 - n - 1) * 60 + 60 - m)
