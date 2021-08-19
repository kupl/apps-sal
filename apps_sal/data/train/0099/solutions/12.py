# Contest No.: 652
# Problem No.: B
# Solver:      JEMINI
# Date:        20200623

import sys
import heapq


def main():
    t = int(input())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        s = sys.stdin.readline().strip()
        if ("1" in s and "0" not in s) or ("1" not in s and "0" in s):
            print(s)
            continue
        lPoint = 0
        while s[lPoint] == "0":
            lPoint += 1
        rPoint = n - 1
        while s[rPoint] == "1":
            rPoint -= 1

        if lPoint > rPoint:
            print(s)
            continue

        if lPoint != n - 1:
            ans = s[:lPoint]
        else:
            ans = ""

        ans += "0"

        if rPoint != n - 1:
            ans += s[rPoint + 1:]
        print(ans)

    return


def __starting_point():
    main()


__starting_point()
