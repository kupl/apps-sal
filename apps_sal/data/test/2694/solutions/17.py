n, m, k = map(int, input().split())
bom = []
for _ in range(k):
    bom.append(list(map(int, input().split())))
count = n + m - 2

if k == 3 or k == 4:
    print('NO')
else:
    can = True
    for b in bom:
        y, x, t, f = b
        if y == 1 and x == 1:
            can = False
    if can:
        sets = {1}
    else:
        sets = set()

    for i in range(1, count + 1):
        for b in bom:
            y, x, t, f = b
            gap = x + y - i - 1
            s_dura = i - t - 1
            if s_dura > 0:
                gap = abs(gap)
                temp = s_dura - gap
                if temp >= 0 and temp % f == 0:
                    if 1 <= abs(i - x + 1) <= n:
                        sets.discard(x)
                    if 1 <= abs(i - y + 1) <= m:
                        sets.discard(abs(i - y + 1))
            if gap == 0:
                sets.discard(x)

        if len(sets) == 0:
            break

        for v in list(sets):
            if v <= i - n + 1:
                sets.remove(v)
            if v + 1 > i - n + 1:
                sets.add(v + 1)
        sets.discard(m + 1)

    if m in sets:
        print("YES")
        print(count)
    else:
        print("NO")
