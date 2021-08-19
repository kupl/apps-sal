(n, s) = map(int, input().split())
s *= 100
ans = -1
for i in range(n):
    (x, y) = map(int, input().split())
    cost = x * 100 + y
    if s < cost:
        continue
    sd = (s - cost) % 100
    ans = max(ans, sd)
print(ans)
