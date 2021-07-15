n, a = map(int, input().split())
a -= 1
t = list(map(int, input().split()))
ans = t[a]
for d in range(1, n):
    if a >= d and a + d < n and t[a - d] and t[a + d]:
        ans += 2
    elif a < d and a + d < n and t[a + d]:
        ans += 1
    elif a >= d and a + d >= n and t[a - d]:
        ans += 1
print(ans)
