(n, h, m) = map(int, input().split())
houses = [h for i in range(n)]
for i in range(m):
    (l, r, x) = map(int, input().split())
    for i in range(l - 1, r):
        houses[i] = min(x, houses[i])
ans = 0
for house in houses:
    ans += house ** 2
print(ans)
