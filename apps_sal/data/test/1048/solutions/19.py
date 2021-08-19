n = int(input())
l = d = u = r = 0
ans = 0
for i in input():
    if i == 'L':
        l += 1
    elif i == 'D':
        d += 1
    elif i == 'U':
        u += 1
    else:
        r += 1
ans += min(l, r) * 2
ans += min(u, d) * 2
print(ans)
