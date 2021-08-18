
def __starting_point():
    n, m, k = map(int, input().split())
    m -= n
    res = 1
    lvl = 0
    while m > 0:
        x = min(k, lvl + 1) + min(n - k, lvl)
        if (x == n):
            res += m // n
            break
        elif (m >= x):
            m -= x
            lvl += 1
            res += 1
        else:
            break
    print(res)


__starting_point()
