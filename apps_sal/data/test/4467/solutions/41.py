def abc091_c():
    n = int(input())
    red = []
    blue = []
    for _ in range(n):
        (a, b) = (int(x) for x in input().split())
        red.append((a, b))
    for _ in range(n):
        (c, d) = (int(x) for x in input().split())
        blue.append((c, d))
    blue = sorted(blue, key=lambda x: x[0])
    ans = 0
    r_used = [False] * n
    for (c, d) in blue:
        match = -1
        y_high = -1
        for (i, (a, b)) in enumerate(red):
            if r_used[i]:
                continue
            if not (a < c and b < d):
                continue
            if y_high < b:
                match = i
                y_high = b
        if match != -1:
            ans += 1
            r_used[match] = True
    print(ans)


def __starting_point():
    abc091_c()


__starting_point()
