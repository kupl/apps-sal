#	!/usr/bin/env python3
#	encoding: UTF-8
#	Modified: <07/Jun/2019 05:47:40 PM>


#	✪ H4WK3yE乡
#	Mohd. Farhan Tahir
#	Indian Institute Of Information Technology (IIIT), Gwalior


import sys


def get_array(): return list(map(int, sys.stdin.readline().split()))


def get_ints(): return list(map(int, sys.stdin.readline().split()))


def input(): return sys.stdin.readline().strip()


def main():
    n = int(input())
    ans = n // 2 + 1
    print(ans)
    r = 0
    c = 1
    for i in range(1, n + 1):
        if i % 2 == 1:
            r += 1
        else:
            c += 1
        print(r, c)


def __starting_point():
    main()

__starting_point()
