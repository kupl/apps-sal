a, b, c, d = list(map(int, input().split()))
m = min(a, c, d)
a -= m
c -= m
d -= m
ans = 256 * m
ans += 32 * min(a,b )
print(ans)

