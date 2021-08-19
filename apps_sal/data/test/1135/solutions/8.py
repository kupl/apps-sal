#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# n = int(input())
#
# a, b = [int(i) for i in input().split()]
#

n = int(input())
slovo = input()
otvet = ''
while slovo != '':
    en = slovo[0]
    if len(slovo) % 2 == 1:
        otvet = otvet + en
    else:
        otvet = en + otvet
    slovo = slovo[1:]
print(otvet)
