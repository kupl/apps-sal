#	!/usr/bin/env python3
#	encoding: UTF-8
#	Modified: <26/Apr/2019 08:18:47 PM>


#	✪ H4WK3yE乡
#	Mohd. Farhan Tahir
#	Indian Institute Of Information Technology (IIIT),Gwalior


# ///==========Libraries, Constants and Functions=============///


import sys


def get_array(): return list(map(int, sys.stdin.readline().split()))


def get_ints(): return map(int, sys.stdin.readline().split())


def input(): return sys.stdin.readline().strip()

# ///==========MAIN=============///


def main():
    n = int(input())
    a = list(input())
    f = get_array()
    flag = False
    for i in range(n):
        x = int(a[i])
        if (x < f[x - 1]):
            flag = True
            a[i] = f[x - 1]
        else:
            if flag == True and x > f[x - 1]:
                break
    print(*a, sep='')


def __starting_point():
    main()


__starting_point()
