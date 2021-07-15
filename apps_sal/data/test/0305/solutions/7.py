a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
ans = 0

if e > f:
    ans += e * min(a, d)
    d -= min(a, d)
    ans += f * min(b, c, d)
else:
    ans += f * min(b, c, d)
    d -= min(b, c, d)
    ans += e * min(a, d)

print(ans)

