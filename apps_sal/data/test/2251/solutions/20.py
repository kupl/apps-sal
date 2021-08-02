from collections import defaultdict, deque, Counter, OrderedDict


def main():
    N = 105
    n, m = map(int, input().split())
    par = [[j for j in range(N)] for i in range(N)]

    def find(a, c):
        if par[c][a] == a:
            return a
        par[c][a] = find(par[c][a], c)
        return par[c][a]

    def merge(a, b, c):
        a = find(a, c)
        b = find(b, c)
        par[c][b] = a

    for i in range(m):
        a, b, c = map(int, input().split())
        a, b = a - 1, b - 1
        merge(a, b, c)

    q = int(input())
    for i in range(q):
        a, b = map(int, input().split())
        a, b, ans = a - 1, b - 1, 0
        for i in range(N):
            if find(a, i) == find(b, i):
                ans += 1
        print(ans)


def __starting_point():
    main()


__starting_point()
