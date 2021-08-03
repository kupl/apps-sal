a, b, c, d, e, f = [int(input())for _ in range(6)]
ans = 0
if e > f:
    m = min(a, d)
    ans += e * m
    d -= m
    print(ans + min(b, c, d) * f)
else:
    m = min(b, c, d)
    ans += f * m
    d -= m
    print(ans + min(a, d) * e)
