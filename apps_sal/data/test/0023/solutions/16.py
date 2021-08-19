#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    a = list(input())
    b = list(input())
    n = len(a)
    if (n < len(b)):
        a.sort()
        a.reverse()
        print(''.join(a))
        return
    b_ = [int(_) for _ in b]
    a.sort()
    a.reverse()
    a_ = [int(_) for _ in a]
    c = [0 for _ in range(n)]
    r = []
    index = 0
    flag = 0
    while index < n:
        now = b_[index]
        if now < 0:
            b_[index] = 0
            index -= 1
            b_[index] -= 1
            r = []
            c = [0 for _ in range(n)]
            index = 0
            continue
        ma = -1
        for i in range(n):
            if c[i]:
                continue
            if a_[i] <= now:
                c[i] = 1
                ma = a_[i]
                break
        if ma is -1:
            b_[index] = 9
            index -= 1
            b_[index] -= 1
            r = []
            c = [0 for _ in range(n)]
            index = 0
            continue
        r.append(ma)
        if ma < int(b[index]):
            flag = 1
            break
        index += 1
    if flag is 1:
        for each in r:
            print(each, end='')
            a_.remove(each)
        for each in a_:
            print(each, end='')
        print()
        return
    for each in r:
        print(each, end='')
    print()


main()
