#!/usr/bin/env python3
from bisect import bisect


def solve(s):
    def processArr(arr):
        r_count = arr.count("R")
        r = sum((r_count - i) % 2 for i in range(len(arr)))
        l = len(arr) - r
        return [0] * (r_count - 1) + [r] + [l] + [0] * (len(arr) - r_count - 1)
    ans = []
    lst = []
    prev = ""
    n = len(s)
    for i in range(n):
        if s[i] == "R" and prev == "L":
            ans.extend(processArr(lst))
            lst.clear()
        lst.append(s[i])
        prev = s[i]
    if lst != []:
        ans.extend(processArr(lst))
    return ans


def main():
    S = input()
    print((*solve(S)))
    return


def __starting_point():
    main()


__starting_point()
