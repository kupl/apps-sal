#!/usr/bin/env python
# -*- coding:utf-8 -*-

import itertools

def main():
    send = input()
    recv = input()

    pos = 0
    for c in send:
        if c == '+':
            pos += 1
        else:
            pos -= 1

    est = 0
    amb = 0
    for c in recv:
        if c == '+':
            est += 1
        elif c == '-':
            est -= 1
        else:
            amb += 1

    remain = pos - est

    prob = 0.0
    if amb == 0:
        if remain == 0:
            prob = 1.0
        else:
            prob = 0.0
    else:
        num = 0
        den = 0
        for seq in itertools.product( ( '+', '-' ), repeat = amb ):
            den += 1
            val = 0
            for c in seq:
                if c == '+':
                    val += 1
                else:
                    val -= 1

            if val == remain:
                num += 1

        prob = num / den

    print( prob )

    return

def __starting_point():
    main()

__starting_point()
