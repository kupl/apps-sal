from collections import Counter
import sys
readline = sys.stdin.readline


def main():
    N, M = map(int, readline().rstrip().split())
    A = list(map(int, readline().rstrip().split()))
    pre = 0
    B = [0]
    for a in A:
        pre += a
        B.append(pre)

    B = [b % M for b in B]
    c = Counter(B)
    res = 0
    for cnt in c.values():
        res += cnt * (cnt - 1) // 2

    print(res)


def __starting_point():
    main()


__starting_point()
