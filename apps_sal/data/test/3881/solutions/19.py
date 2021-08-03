#!/usr/bin/env python3

alphabet = list('abcdef')


def all_strs_gen(n):
    s = ['a'] * n
    for i in range(0, len(alphabet) ** n):
        yield ''.join(s)
        for j in range(0, n):
            if s[j] == alphabet[-1]:
                s[j] = alphabet[0]
            else:
                s[j] = chr(ord(s[j]) + 1)
                break


n, q = [int(x) for x in input().split()]
ops = {}
for i in range(0, q):
    op, s = input().split()
    ops[op] = s


def compress(s):
    while s[0:2] in ops:
        # print(s)
        s = ops[s[0:2]] + s[2:]
    # print(s)
    # print()
    return s


count = 0
for s in all_strs_gen(n):
    if 'a' == compress(s):
        count += 1

print(count)
