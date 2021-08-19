(a, b) = list(map(float, input().split()))
n = int(input())
ans = 100000000.69
ansidx = -1
for i in range(n):
    (x, y, v) = list(map(float, input().split()))
    ans = min(ans, ((x - a) ** 2 + (y - b) ** 2) ** (1 / 2) / v)
print(ans)
