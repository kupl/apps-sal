#!/usr/bin/env python3
W, a, b = list(map(int, input().split()))

a_l = a
a_r = a + W
b_l = b
b_r = b + W

if b_r < a_l:
    print((abs(b_r - a_l)))
elif a_r < b_l:
    print((abs(a_r - b_l)))
else:
    print((0))
