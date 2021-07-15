def solve(k, x, y):
    if k % 2 == 0 and (x + y) % 2 == 1:
        print((-1))
        return

    ans = []
    abx, aby = abs(x), abs(y)
    mh = abx + aby
    xx, yy = 0, 0

    if mh % k == 0:
        d = (mh - 1) // k + 1
        for _ in range(d - 1):
            dx, dy = abs(abx - xx), abs(aby - yy)
            if dx > 0:
                if dx >= k:
                    xx += k
                else:
                    xx += dx
                    yy += k - dx
            else:
                yy += k
            ans.append((xx, yy))
        ans.append((abx, aby))
        print_ans(ans, x, y)
        return

    d = (mh - 1) // k + 1

    if k % 2 == 1 and mh % 2 != max(2, d) % 2:
        if abx > aby:
            xx += min(k, abx)
            yy += k - min(k, abx)
        else:
            yy += min(k, aby)
            xx += k - min(k, aby)
        ans.append((xx, yy))

    for _ in range(d - 2):
        dx, dy = abs(abx - xx), abs(aby - yy)
        if dx > dy:
            if abx > xx:
                xx += k
            else:
                xx -= k
        else:
            if aby > yy:
                yy += k
            else:
                yy -= k
        ans.append((xx, yy))

    dx, dy = abs(abx - xx), abs(aby - yy)
    mhh = (dx + dy) // 2
    if dx > dy:
        if abx > xx:
            xx += mhh
        else:
            xx -= mhh
        if aby > yy:
            yy -= k - mhh
        else:
            yy += k - mhh
    else:
        if aby > yy:
            yy += mhh
        else:
            yy -= mhh
        if abx > xx:
            xx -= k - mhh
        else:
            xx += k - mhh
    ans.append((xx, yy))
    ans.append((abx, aby))

    print_ans(ans, x, y)


def print_ans(ans, x, y):
    print((len(ans)))
    for dx, dy in ans:
        if x < 0:
            dx = -dx
        if y < 0:
            dy = -dy
        print((dx, dy))


k = int(input())
x, y = list(map(int, input().split()))
solve(k, x, y)

