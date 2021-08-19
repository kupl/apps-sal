def I():
    return map(int, input().split())


(n, t) = I()
a = list(I())
ans = 0
x = min(a)
while t >= x:
    y = t
    z = 0
    for i in a:
        if y >= i:
            z += 1
            y -= i
    r = t // (t - y)
    ans += z * r
    t -= (t - y) * r
print(ans)
