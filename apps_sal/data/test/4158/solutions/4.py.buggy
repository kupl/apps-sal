#!/usr/bin/env python3
from sys import stdin, stdout


def rint():
    return list(map(int, stdin.readline().split()))
#lines = stdin.readlines()


n = int(input())

x = set(rint())
x_list = list(x)
x_list.sort()
# print(x)
# print(x_list)
max_len = 1
for i in range(len(x_list)):
    start = x_list[i]
    for j in range(0, 1000):
        candidate = [start]
        next = start + 2**j
        if next > x_list[-1]:
            break
        if next in x:
            candidate.append(next)
            next = start + 2**(j + 1)
            if next in x:
                candidate.append(next)
                print(3)
                print(*candidate)
                return
            else:
                ans = candidate
                max_len = 2

if max_len == 2:
    print(2)
    print(*ans)
else:
    print(1)
    print(x_list[0])
