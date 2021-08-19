(n, m) = map(int, input().split())
ans = n
for i in range(m):
    (x, y) = map(int, input().split())
    ans = min(ans, y - x + 1)
print(ans)
for i in range(n):
    print(i % ans, end=' ')
print()
