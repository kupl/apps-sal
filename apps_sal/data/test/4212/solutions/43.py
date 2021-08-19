import sys


def IS():
    return sys.stdin.readline().rstrip()


def II():
    return int(IS())


def MII():
    return list(map(int, IS().split()))


def main():
    (n, m, q) = MII()
    query = [MII() for _ in range(q)]

    def calc_point(lst):
        sumv = 0
        for (a, b, c, d) in query:
            if lst[b - 1] - lst[a - 1] == c:
                sumv += d
        return sumv

    def dfs(lst):
        if len(lst) == n:
            return calc_point(lst)
        point = 0
        last_elm = lst[-1] if len(lst) > 0 else 1
        for i in range(last_elm, m + 1):
            point = max(point, dfs(lst + [i]))
        return point
    print(dfs([]))


def __starting_point():
    main()


__starting_point()
