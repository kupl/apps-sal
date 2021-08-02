a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

if(e >= f):
    ans = min(a, d) * e
    d -= min(a, d)
    ans += min(min(b, c), d) * f
    print(ans)
else:
    ans = min(min(b, c), d) * f
    d -= min(min(b, c), d)
    ans += min(a, d) * e
    print(ans)
