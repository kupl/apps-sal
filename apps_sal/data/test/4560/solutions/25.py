#!/usr/bin/env python3

n = int(input())
a = int(input())

num = n % 500

if num > a:
    print("No")
else:
    print("Yes")
