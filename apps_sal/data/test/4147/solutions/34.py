def main():
    (n, a, b, c) = list(map(int, input().split()))
    L = [int(input()) for _ in range(n)]
    INF = 1000000

    def dfs(i, la, lb, lc):
        if i == n:
            return abs(la - a) + abs(lb - b) + abs(lc - c) if min(la, lb, lc) > 0 else INF
        res = []
        res.append(dfs(i + 1, la, lb, lc))
        res.append(dfs(i + 1, la + L[i], lb, lc) + 10 if la != 0 else dfs(i + 1, la + L[i], lb, lc))
        res.append(dfs(i + 1, la, lb + L[i], lc) + 10 if lb != 0 else dfs(i + 1, la, lb + L[i], lc))
        res.append(dfs(i + 1, la, lb, lc + L[i]) + 10 if lc != 0 else dfs(i + 1, la, lb, lc + L[i]))
        return min(res)
    print(dfs(0, 0, 0, 0))


def __starting_point():
    main()


__starting_point()
