
[n, m] = map(int, input().split())
ans = 1e9
for i in range(m):
    [l, r] = map(int, input().split())
    ans = min(ans, r - l + 1)
print(ans)
for i in range(n):
    print(i % ans, end = " ")
print()
