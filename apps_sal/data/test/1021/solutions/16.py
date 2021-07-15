
# -*- coding: utf-8 -*-
# @Date    : 2019-02-08 08:18:25
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

from sys import stdin

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]

nb_elements = int(input())
first = [int(x) for x in input().split()]
secon = [int(x) for x in input().split()]
if first[-1] != secon[-1] or first[0] != secon[0]:
    print("No")
else:
    first_1 = [y - x for x, y in zip(first, first[1:])]
    secon_1 = [y - x for x, y in zip(secon, secon[1:])]
    #print(first_1, secon_1)
    print(["No", "Yes"][sorted(first_1) == sorted(secon_1)])

