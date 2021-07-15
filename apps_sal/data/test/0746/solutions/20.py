a, b = map(int, input().split())
n = int(input())
ans = 100000000
for i in range(n):
    x, y, v = map(int, input().split())
    d = ((x - a) ** 2 + (y - b) ** 2) ** 0.5
    ans = min(ans, d * 1. / v)
print(ans)
