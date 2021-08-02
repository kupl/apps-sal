from collections import defaultdict
import sys
def input(): return sys.stdin.readline().strip()


def main():
    N, P = map(int, input().split())
    S = input()

    ans = 0
    if P in [2, 5]:
        for i, c in enumerate(S[::-1]):
            if int(c) % P == 0:
                ans += N - i
    else:
        d = defaultdict(int)
        d[0] = 1
        num = 0
        ten = 1
        for c in S[::-1]:
            num += int(c) * ten
            num %= P
            d[num] += 1
            ten *= 10
            ten %= P

        ans = sum([d[i] * (d[i] - 1) // 2 for i in range(P)])

    print(ans)


def __starting_point():
    main()


__starting_point()
