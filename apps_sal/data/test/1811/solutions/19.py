
# -*- coding: utf-8 -*-
# @Date    : 2019-01-24 10:40:45
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

from sys import stdin

max_val = int(10e12)
min_val = int(-10e12)


def read_int(): return int(stdin.readline())
def read_ints(): return [int(x) for x in stdin.readline().split()]
def read_str(): return input()
def read_strs(): return [x for x in stdin.readline().split()]


points, jumps = read_ints()
print(["NO", "YES"][len(max(read_str().split("."), key=len)) < jumps])
