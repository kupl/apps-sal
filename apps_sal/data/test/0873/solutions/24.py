#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input())

code_old = input()
code_new = input()

steps = 0

for i in range(n):
    steps_i = abs(int(code_new[i]) - int(code_old[i]))
    if steps_i > 5:
        steps_i = 10 - steps_i
    steps += steps_i

print(steps)

