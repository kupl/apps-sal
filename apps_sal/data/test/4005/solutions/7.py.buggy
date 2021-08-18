#!/usr/bin/env python3

import sys

w = [int(i) for i in input().split()]
b1 = [int(i) for i in input().split()]
b2 = [int(i) for i in input().split()]


def is_inside(r_in, r_out):
    return (r_out[0] <= r_in[0] <= r_out[2]) and (
        r_out[1] <= r_in[1] <= r_out[3]) and (
            r_out[0] <= r_in[2] <= r_out[2]) and (
                r_out[1] <= r_in[3] <= r_out[3])


def bisects(r_in, r_out):
    return ((r_out[0] <= r_in[0] <= r_out[2])
            and (r_out[0] <= r_in[2] <= r_out[2])) or (
                (r_out[1] <= r_in[1] <= r_out[3]) and (
                    r_out[1] <= r_in[3] <= r_out[3]))


if is_inside(w, b1) or is_inside(w, b2):
    print('NO')
    return


if b1[0] <= w[0] <= b1[2] and b1[0] <= w[2] <= b1[2]:
    if b1[1] <= w[1] <= b1[3]:
        w[1] = b1[3]
    elif b1[1] <= w[3] <= b1[3]:
        w[3] = b1[1]
elif b1[1] <= w[1] <= b1[3] and b1[1] <= w[3] <= b1[3]:
    if b1[0] <= w[0] <= b1[2]:
        w[0] = b1[2]
    elif b1[0] <= w[2] <= b1[2]:
        w[2] = b1[0]
elif b2[0] <= w[0] <= b2[2] and b2[0] <= w[2] <= b2[2]:
    if b2[1] <= w[1] <= b2[3]:
        w[1] = b2[3]
    elif b2[1] <= w[3] <= b2[3]:
        w[3] = b2[1]
elif b2[1] <= w[1] <= b2[3] and b2[1] <= w[3] <= b2[3]:
    if b2[0] <= w[0] <= b2[2]:
        w[0] = b2[2]
    elif b2[0] <= w[2] <= b2[2]:
        w[2] = b2[0]

if is_inside(w, b1) or is_inside(w, b2):
    print('NO')
    return

print('YES')
