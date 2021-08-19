(a, b, t) = map(int, input().split())
ans = 0
i = 1
while i * a <= t + 0.5:
    ans += b
    i += 1
print(ans)
