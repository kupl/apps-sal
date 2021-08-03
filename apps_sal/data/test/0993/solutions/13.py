from collections import defaultdict


def main():
    N, M = list(map(int, input().split(' ')))
    A = list(map(int, input().split(' ')))
    d = defaultdict(int)
    d[0] += 1
    cs = 0
    for i in range(N):
        cs += A[i]
        cs %= M
        d[cs] += 1
    ans = 0
    for v in d.values():
        ans += v * (v - 1) // 2
    print(ans)


def __starting_point():
    main()


__starting_point()
