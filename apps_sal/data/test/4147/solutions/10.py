import sys
def input(): return sys.stdin.readline().rstrip()
def input_nums(): return list(map(int, input().split()))


INF = 10**9


def main():
    N, A, B, C = input_nums()
    ll = [int(input()) for _ in range(N)]

    def dfs(idx, a, b, c):
        if idx == N:
            return abs(a - A) + abs(b - B) + abs(c - C) - 30 if min(a, b, c) > 0 else INF
        ret0 = dfs(idx + 1, a, b, c)
        ret1 = dfs(idx + 1, a + ll[idx], b, c) + 10
        ret2 = dfs(idx + 1, a, b + ll[idx], c) + 10
        ret3 = dfs(idx + 1, a, b, c + ll[idx]) + 10
        return min(ret0, ret1, ret2, ret3)

    print(dfs(0, 0, 0, 0))


def __starting_point():
    main()


__starting_point()
