#!/usr/bin/env python3

S = input()
ret = ''
for i in range(len(S)):
    if S[i] == '0': ret += '0'
    elif S[i] == '1': ret += '1'
    else: ret = ret[:-1]

print(ret)
