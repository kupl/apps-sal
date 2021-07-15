n = int(input())
a = [0] * n
p = [0] * n
for i in range(n):
    a[i], p[i] = map(int, input().split())
minP = [p[0]] * n
for i in range(1, n):
    minP[i] = min(minP[i - 1], p[i])
ans = 0
for i in range(n):
    ans += a[i] * minP[i]
print(ans)
