#!/usr/bin/env python3

import sys

N = int(input())
l = input().split()
is_zero = True
for i in l:
    if i == '0':
        break
else:
    is_zero = False
if is_zero:
    print('0')
    return

def are_all_zero(s):
    for c in s:
        if c != '0':
            return False
    return True

times = 0
ugly = '1'
for i in l:
    if are_all_zero(i[1:]) and i[0] == '1':
        times += len(i) - 1
    else:
        ugly = i
answer = ugly + '0'*times
print(answer)

