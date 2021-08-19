# cost e, a,d
# cost f, b,c,d

a, b, c, d, e, f = [int(input()) for i in range(6)]

q = min(a, d)
dd = d - q
ans = e * q + f * min(b, c, dd)

w = min(b, c, d)
dd = d - w
ans = max(ans, e * min(a, dd) + f * w)

print(ans)
