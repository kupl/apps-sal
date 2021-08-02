a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
ans = 0
if(f > e):
    m = min(b, c, d)
    ans += m * f
    d -= m
    m = min(d, a)
    ans += m * e
else:
    m = min(d, a)
    ans += m * e
    d -= m
    m = min(b, c, d)
    ans += m * f
print(ans)
