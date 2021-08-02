x, y = list(map(int, input().split(' ')))

ok = []
while y % x in [0, 1, -1 + x]:
    if y % x == 0:
        y //= x
        ok.append(0)
    elif y % x == 1:
        y = (y - 1) // x
        ok.append(1)

    else:
        y = (y + 1) // x
        ok.append(-1)

    if y == 0:
        break

if y == 0:
    print("YES")

else:
    print("NO")
