(a, b, c, d) = [int(x) for x in input().split()]
ans = a / b
ac = step = (b - a) / b * (d - c) / d
while ac > 1e-07:
    ans += a / b * ac
    ac *= step
print(ans)
