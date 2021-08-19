(n, m) = map(lambda x: int(x), input().split())
ans = n
for i in range(m):
    (l, r) = map(lambda x: int(x), input().split())
    ans = min(ans, r - l + 1)
print(ans)
for i in range(n):
    print(i % ans, end=' ')
