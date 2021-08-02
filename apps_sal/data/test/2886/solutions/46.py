# -*- coding: utf-8 -*-

import io
import sys
import math


def solve(s):
    # implement process
    len_s = len(s)
    a, b = -1, -1
    for i in range(len_s):
        if len_s - i > 1 and s[i] == s[i + 1]:
            a, b = i + 1, i + 2
            break
        if len_s - i > 2 and s[i] == s[i + 2]:
            a, b = i + 1, i + 3
            break
    return f"{a} {b}"


def main():
    # input
    s = input()
    # process
    ans = str(solve(s))

    # output
    print(ans)
    return ans


### DEBUG I/O ###
_DEB = 0   # 1:ON / 0:OFF

_INPUT = """\
aba
"""
_EXPECTED = """\
2 5
"""


def logd(str):
    """usage:
    if _DEB: logd(f"{str}")
    """
    if _DEB: print(f"[deb] {str}")

### MAIN ###


def __starting_point():
    if _DEB:
        sys.stdin = io.StringIO(_INPUT)
        print("!! Debug Mode !!")

    ans = main()

    if _DEB:
        print()
        if _EXPECTED.strip() == ans.strip(): print("!! Success !!")
        else: print(f"!! Failed... !!\nANSWER:   {ans}\nExpected: {_EXPECTED}")


__starting_point()
