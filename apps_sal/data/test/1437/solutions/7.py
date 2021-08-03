#!/usr/bin/env python3
# -*- coding: utf-8 -*-

str_in = input()


def decode_char(c):
    if '0' <= c <= '9':
        return ord(c) - ord('0')
    elif 'A' <= c <= 'Z':
        return (ord(c) - ord('A')) + 10
    elif 'a' <= c <= 'z':
        return (ord(c) - ord('a')) + 36
    elif '-' == c:
        return 62
    elif '_' == c:
        return 63
    assert False


result_num = 0
for c in str_in:
    res_str = "{0:06b}".format(decode_char(c))
    result_num += sum(1 for i in res_str if i == '0')

print(pow(3, result_num, 10**9 + 7))
