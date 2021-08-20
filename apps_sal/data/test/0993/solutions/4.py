import sys
import collections
input = sys.stdin.readline


def main():
    (N, M) = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    B = [0]
    for a in A:
        B.append((B[-1] + a) % M)
    c = collections.Counter(B)
    ans = 0
    for k in list(c.keys()):
        if c[k] <= 1:
            continue
        ans += c[k] * (c[k] - 1) // 2
    print(ans)


def __starting_point():
    main()


__starting_point()
