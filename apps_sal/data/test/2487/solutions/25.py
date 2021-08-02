import sys
input = sys.stdin.readline
n = int(input())
ans = 0
for i in range(n):
    ans += (i + 1) * (n - i)
for i in range(n - 1):
    a, b = map(int, input().split())
    a, b = min(a, b), max(a, b)
    ans -= a * (n - b + 1)
print(ans)
