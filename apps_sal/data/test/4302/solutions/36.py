(a, b) = list(map(int, input().split()))
ans = 0
ans = max(a, b)
c = max(a, b) - 1
ans += max(min(a, b), c)
print(ans)
