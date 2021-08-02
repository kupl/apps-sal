n = int(input())

ans = [[cx, cy, -1] for cx in range(101) for cy in range(101)]
zeroes = []

for i in range(n):
    x, y, h = list(map(int, input().split()))

    if h > 0:
        delete = []

        for j in range(len(ans)):
            cx, cy, ch = ans[j]

            calcH = h + abs(x - cx) + abs(y - cy)
            if ch == -1:
                ans[j][2] = calcH
            else:
                if ch != calcH:
                    delete.append(j)

        while len(delete) > 0:
            del ans[delete.pop()]
    else:
        zeroes.append([x, y])

for x, y in zeroes:
    delete = []

    for j in range(len(ans)):
        cx, cy, ch = ans[j]

        if ch - abs(x - cx) - abs(y - cy) > 0:
            delete.append(j)

    while len(delete) > 0:
        del ans[delete.pop()]

print(" ".join(map(str, ans[0])))
