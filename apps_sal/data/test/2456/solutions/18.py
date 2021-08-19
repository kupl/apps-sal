import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    (n, r) = map(int, input().split())
    if r < n:
        print(r * (r + 1) // 2)
    else:
        print(n * (n - 1) // 2 + 1)
