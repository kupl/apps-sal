import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    (n, x, y) = map(int, input().split())
    ans2 = max(min(x + y - 1, n), 1)
    ans1 = min(max(1, x + y - n + 1), n)
    print(ans1, ans2)
