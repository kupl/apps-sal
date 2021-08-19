#	!/usr/bin/env python3
#	coding: UTF-8
#	Modified: <18/Feb/2019 09:13:07 PM>


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
    n = int(input())
    arr = get_array()
    #from collections import Counter
    maxi = max(arr)
    mx, curr = 0, 0
    for i in range(n):
        if arr[i] == maxi:
            curr += 1
            mx = max(mx, curr)
        else:
            curr = 0
    print(mx)


def __starting_point():
    main()


__starting_point()
