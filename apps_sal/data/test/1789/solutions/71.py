#!/usr/bin/env python
#-*- coding: utf-8 -*-

def __starting_point():
    a, b, x, y = list(map(int, input().split()))
    y = min(y, 2*x)
    print((x+min(abs(a-b), abs(a-1-b))*y))

__starting_point()
