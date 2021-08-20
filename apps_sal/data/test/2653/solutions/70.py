import sys
sys.setrecursionlimit(10000000)


def main():
    (n, q) = list(map(int, input().split()))
    Ki = [[] for i in range(n)]
    for _ in range(n - 1):
        (a, b) = list(map(int, input().split()))
        Ki[a - 1] += [b - 1]
        Ki[b - 1] += [a - 1]
    ans = [0] * n
    for _ in range(q):
        (p, x) = list(map(int, input().split()))
        ans[p - 1] += x

    def add(N=0, L=-1):
        for k in Ki[N]:
            if k != L:
                ans[k] += ans[N]
                add(k, N)
    add()
    print(' '.join([str(a) for a in ans]))


def __starting_point():
    main()


__starting_point()
