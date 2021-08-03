#!/usr/bin/env python3
def main():
    def expected_val(limit):
        return (1 + limit) / 2

    N, K = list(map(int, input().split()))
    P = [int(x) for x in input().split()]

    lst = [0]
    res = 0
    for p in P:
        # res += (p + 1) / 2
        res += expected_val(p)
        lst.append(res)
    ans = 0
    for i in range(N - K + 1):
        res = lst[i + K] - lst[i]
        ans = res if res > ans else ans
    print(ans)


def __starting_point():
    main()


__starting_point()
