(a, b, c, d) = map(int, input().split())
mini = min(a, c, d)
ans = 0
ans += mini * 256
a -= mini
c -= mini
d -= mini
mini = min(a, b)
ans += mini * 32
print(ans)
