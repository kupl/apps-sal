#!/usr/bin/env python3

n = int(input())
s = input()

if s == '0':
    print('0')
elif s[0] == '1':
    print('1' + s[1:].replace('1', ''))
