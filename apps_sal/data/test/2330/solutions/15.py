import sys
import math


def input():
    return sys.stdin.readline()[:-1]


def main():
    q = int(input())
    for _ in range(q):
        (n, m) = list(map(int, input().split()))
        a = list(map(int, input().split()))
        if n > m or n == 2:
            print(-1)
        else:
            ansv = 2 * sum(a)
            ans = [[k, k + 1] for k in range(1, n)]
            ans.append([n, 1])
            b = sorted([[a[k], k + 1] for k in range(n)])
            for k in range(m - n):
                ans.append([b[0][1], b[1][1]])
            print(ansv + (m - n) * (b[0][0] + b[1][0]))
            for e in ans:
                print(*e)


def __starting_point():
    main()


__starting_point()
