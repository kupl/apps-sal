(t, s, q) = map(int, input().split())
ans = 1
while s * q < t:
    ans += 1
    s *= q
print(ans)
