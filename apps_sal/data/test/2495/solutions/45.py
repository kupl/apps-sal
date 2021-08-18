
def ri():
    return int(input())


def rl():
    return list(input().split())


def rli():
    return list(map(int, input().split()))


def solve(la):
    ans = 0
    s = la[0]
    for i in range(1, len(la)):
        a = la[i]
        ns = s + a
        if s * ns < 0:
            s = ns
            continue
        ans += abs(ns) + 1
        if ns < 0:
            ns += abs(ns) + 1
        else:
            ns -= abs(ns) + 1
        s = ns
    return ans


def main():
    n = ri()
    la = rli()
    first = la[0]

    ans1 = 0
    if first <= 0:
        ans1 += abs(first) + 1
        la[0] = 1
    ans1 += solve(la)

    ans2 = 0
    la[0] = first
    if first >= 0:
        ans2 += abs(first) + 1
        la[0] = -1
    ans2 += solve(la)
    print((min(ans1, ans2)))


def __starting_point():
    main()


__starting_point()
