from collections import defaultdict


def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def main():
    n, x = Input()
    l = Input()
    d = defaultdict(int)
    d[0] = 0
    ans = 0

    for i in range(1, n + 1):
        d[i] = d[i - 1] + l[i - 1]

    for i in d.values():
        if i <= x: ans += 1

    print(ans)


main()
