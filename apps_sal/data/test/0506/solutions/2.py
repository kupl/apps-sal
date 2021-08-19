#!/usr/bin/env python3

a, b = list(map(int, input().split(' ')))

ships_num = 0

while b != 0:
    ships_num += a // b
    a, b = b, a % b

print(ships_num)
