#!/usr/bin/env python3
from itertools import dropwhile

def main():
    n = int(input())
    lst = [bool(int(x)) for x in input().split()]
    lst = list(dropwhile(lambda x: not x, lst))

    if not lst:
        print(0)
        return

    ans = 1
    cnt = 1

    for x in lst:
        if x:
            if cnt > 1:
                ans *= cnt
                cnt = 1
        else:
            cnt += 1

    print(ans)

def __starting_point():
    main()

__starting_point()
