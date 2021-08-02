3
#coding: utf-8

A, B, C, X, Y = (int(x) for x in input().split())

ret = 0
if A + B > C * 2:
    m = min(X, Y)
    X -= m
    Y -= m
    ret += m * C * 2

if X > 0:
    if A > C * 2:
        ret += X * C * 2
    else:
        ret += X * A

if Y > 0:
    if B > C * 2:
        ret += Y * C * 2
    else:
        ret += Y * B

print(ret)
