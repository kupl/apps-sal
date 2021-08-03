c, v0, v1, a, l = list(map(int, input().split()))

ans = 0
v = v0
p = 0
while p < c:
    p = max(p - l, 0)
    p += v
    v = min(v + a, v1)
    ans += 1

print(ans)
