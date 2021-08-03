from collections import defaultdict


def solve():
    n, T = list(map(int, input().split()))
    a = list(map(int, input().split()))
    white = defaultdict(int)
    black = defaultdict(int)
    ans = [0] * n
    for i, x in enumerate(a):
        if white[T - x] > black[T - x]:
            black[x] += 1
            ans[i] = 1
        else:
            white[x] += 1
            ans[i] = 0
    print(*ans)
    return


def main():
    T = int(input())
    for i in range(T):
        solve()
    return


def __starting_point():
    main()


__starting_point()
