a, b, c, d = map(int, input().split())
x = min(a, c, d)
ans = x * 256
a -= x
c -= x
d -= x
ans += min(a, b) * 32
print(ans)
