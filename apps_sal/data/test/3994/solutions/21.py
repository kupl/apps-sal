import sys
import math


def main():
    def input():
        return sys.stdin.readline()[:-1]
    n = int(input())
    s = [int(x) for x in input()]
    l = []
    for k in range(n):
        l.append(list(map(int, input().split())))
    ans = s.count(1)
    for t in range(1000):
        for k in range(n):
            if t < l[k][1]:
                pass
            else:
                if (t - l[k][1]) % l[k][0] == 0:
                    if s[k] == 1:
                        s[k] = 0
                    else:
                        s[k] = 1
        ans = max(ans, s.count(1))
    print(ans)


def __starting_point():
    main()


__starting_point()
