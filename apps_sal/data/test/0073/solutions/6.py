c, v0, v1, a, l = map(int, input().split())
ans, cur = 1, v0
while cur < c:
    v0 = min(v1, v0 + a)
    cur += v0 - l
    ans += 1

print(ans)
