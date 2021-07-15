# -*- coding: utf-8 -*-
# a = int(input())
# b, c = map(int, input().split())
# 文字列の入力
# s = input()
# 出力
# print("{} {}".format(a+b+c, s))


N = int(input())
a = list(map(int, input().split()))

ans = a[0]

from math import gcd

for aval in a:
    ans = gcd(ans, aval)

print(ans)
