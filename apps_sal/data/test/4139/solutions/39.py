import sys


def IS():
    return sys.stdin.readline().rstrip()


def II():
    return int(IS())


def main():
    n = II()

    def dfs(cur, use):
        counter = 0

        def dfs_(cur, use):
            nonlocal counter
            if cur > n:
                return None
            if use == 7:
                counter += 1
            dfs_(cur * 10 + 7, use | 1)
            dfs_(cur * 10 + 5, use | 2)
            dfs_(cur * 10 + 3, use | 4)
        dfs_(cur, use)
        return counter
    print(dfs(0, 0))


def __starting_point():
    main()


__starting_point()
