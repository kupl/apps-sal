# -*- coding: utf-8 -*-
s = input()
lr_same = (s[0] == s[-1])
odd = len(s)%2

if lr_same ^ odd:
    print("First")
else:
    print("Second")
