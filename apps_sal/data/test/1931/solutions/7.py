# Contest No.: 639
# Problem No.: B
# Solver:      JEMINI
# Date:        20200503

import sys


def main():
    t = int(input())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        ans = 0
        while n > 1:
            cnt = 1
            temp = 2
            while n >= (temp + cnt + 2 * (cnt + 1)):
                temp += cnt + 2 * (cnt + 1)
                cnt += 1
            n -= temp
            ans += 1
        print(ans)

    return


def __starting_point():
    main()


__starting_point()
