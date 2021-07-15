#!/usr/bin/env python
# coding: utf-8

def ri():
    return int(input())

def rl():
    return list(input().split())

def rli():
    return list(map(int, input().split()))

def main():
    t = ri()
    for i in range(t):
        n = ri()
        la = rli()
        if n % 2 == 1:
            print("Second")
            continue
        count = {}
        for a in la:
            count.setdefault(a, 0)
            count[a] += 1
        ok = True
        for v in list(count.values()):
            if v % 2 == 1:
                ok = False
                break
        if ok:
            print("Second")
        else:
            print("First")



def __starting_point():
    main()

__starting_point()
