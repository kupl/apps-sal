def run():
    n, s = [int(x) for x in input().split()]
    d = [[int(x) for x in input().split()] for _ in range(n)]

    first = d[0]
    first = first[0] * 60 + first[1]
    if first >= s + 1:
        print(0, 0)
        return

    for i in range(n - 1):
        lft, rgt = d[i], d[i + 1]
        lft = lft[0] * 60 + lft[1]
        rgt = rgt[0] * 60 + rgt[1]

        if rgt - lft >= (s + 1) * 2:
            ans = lft + s + 1
            print(ans // 60, ans % 60)
            return

    rgt = d[-1]
    rgt = rgt[0] * 60 + rgt[1]
    ans = rgt + s + 1
    print(ans // 60, ans % 60)


run()
