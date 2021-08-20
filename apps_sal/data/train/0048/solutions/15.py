import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    (x, y, k) = map(int, input().split())
    needed = k + y * k
    trades = (needed - 1 + (x - 2)) // (x - 1)
    trades += k
    print(trades)
