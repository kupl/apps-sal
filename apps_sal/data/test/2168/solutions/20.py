
# -*- coding: utf-8 -*-
# @Date    : 2018-12-10 10:06:33
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


nb_companies = read_int()
employees = []
maxs = 0
for i in range(nb_companies):
    values = read_ints()
    nb_employee = values[0]
    salaries = values[1:]
    max_s = max(salaries)
    maxs = max(max_s, maxs)
    employees.append((nb_employee, max_s))
adjustment = 0
for i in employees:
    adjustment += i[0] * (maxs - i[1])
print(adjustment)
