
def buy(n, t, c, s):
    if len(c) == 0:
        return 0
    ans = 0
    if t >= s:
        ans += n * (t // s)
        t %= s
    nc = []
    for i in range(n):
        if t >= c[i]:
            nc.append(c[i])
            t -= c[i]
            ans += 1
        else:
            s -= c[i]
    ans += buy(len(nc), t, nc, s)
    return ans


def main():
    n, t = [int(x) for x in input().split(" ")]
    c = list([int(x) for x in input().split(" ")])
    s = sum(c)

    print(buy(n, t, c, s))


def __starting_point():
    main()


__starting_point()
