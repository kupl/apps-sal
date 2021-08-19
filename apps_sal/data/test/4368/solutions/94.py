(n, k) = map(int, input().split())
ans = 1
while k ** ans <= n:
    ans += 1
print(ans)
