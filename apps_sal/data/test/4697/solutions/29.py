n, m = map(int, input().split())
ans = min(n, m // 2)
m -= ans * 2
ans += max(0, m // 4)
print(ans)
