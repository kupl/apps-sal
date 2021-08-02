gans = []
for _ in range(int(input())):
    y, x = list(map(int, input().split()))
    c2, c3, c4, c5, c6, c1 = list(map(int, input().split()))
    for i in range(6):
        c1 = min(c1, c6 + c2)
        c2 = min(c2, c1 + c3)
        c3 = min(c3, c2 + c4)
        c4 = min(c4, c3 + c5)
        c5 = min(c5, c4 + c6)
        c6 = min(c6, c5 + c1)
    if x == 0 and y == 0:
        gans.append(0)
        continue
    elif x == 0:
        if y > 0:
            ans = y * c1
        else:
            ans = -y * c4
        gans.append(ans)
        continue
    elif y == 0:
        if x > 0:
            ans = x * c3
        else:
            ans = -x * c6
        gans.append(ans)
        continue
    if x * y > 0:
        if x > 0:
            a, b, c = c1, c2, c3
        else:
            a, b, c = c4, c5, c6
            x = -x
            y = -y
        ans = min(x, y) * b
        if x > y:
            ans += (x - y) * c
        else:
            ans += (y - x) * a
        gans.append(ans)
    else:
        if x < 0:
            ans = -c6 * x + c1 * y
        else:
            ans = -c4 * y + c3 * x
        gans.append(ans)
print('\n'.join(map(str, gans)))
