n, m, s, f = list(map(int, input().split()))
c, t1 = 1, 0
ans = ""
t = 1
while s != f and t1 < m:
    t, l, r = list(map(int, input().split()))
    # print(ans)
    while t != c:
        if s < f:
            ans += "R"
            s += 1
        else:
            ans += "L"
            s -= 1
        if s == f:
            break
        c += 1
    if s < f:
        if s >= l - 1 and s <= r:
            ans += "X"
        else:
            ans += "R"
            s += 1
    elif s > f:
        if s <= r + 1 and s >= l:
            ans += "X"
        else:
            ans += "L"
            s -= 1
    c += 1
    t1 += 1
if s < f:
    ans += "R" * (f - s)
elif s > f:
    ans += "L" * (s - f)
print(ans)
