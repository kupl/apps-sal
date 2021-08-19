#!/usr/local/bin/python3
# https://atcoder.jp/contests/abc086/tasks/abc086_b
import math

a, b = input().split()

if math.sqrt(int(a + b)).is_integer():
    print("Yes")
else:
    print("No")
