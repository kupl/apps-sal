a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
ans = 0
if f > e:
    ans += min(d,c,b)*f
    d -= min(d,c,b)
    ans += min(a,d)*e
else:
    ans += min(a,d)*e
    d -= min(a,d)
    ans += min(b,c,d)*f
print(ans)
