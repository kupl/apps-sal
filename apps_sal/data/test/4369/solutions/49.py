# coding: utf-8
# Your code here!
n = int(input())

amari = n % 2

if amari > 0:
    print((n // 2 + 1))
else:
    print((n // 2))
