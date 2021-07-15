#	!/usr/bin/env python3
#	coding: UTF-8
#	Modified: <18/Feb/2019 09:19:08 PM>


#	✪ H4WK3yE乡
#	Mohd. Farhan Tahir
#	Indian Institute Of Information Technology (IIIT),Gwalior

#	Question Link
#
#

# ///==========Libraries, Constants and Functions=============///


import sys

inf = float("inf")
mod = 1000000007


def get_array(): return list(map(int, sys.stdin.readline().split()))


def get_ints(): return list(map(int, sys.stdin.readline().split()))


def input(): return sys.stdin.readline()

# ///==========MAIN=============///


def main():
    n, m, k = get_ints()
    arr = get_array()
    arr.sort()
    if m <= k:
        print(arr[-1] * m)
        return
    x = arr[-1] * k + arr[-2]
    p = m // (k + 1)
    ans = x * p
    p = m % (k + 1)
    ans += (arr[-1] * p)
    print(ans)


def __starting_point():
    main()

__starting_point()
