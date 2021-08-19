#!/usr/bin/env python3
import string

N = int(input().split()[0])
a_list = list(string.ascii_lowercase)

amari_list = []
n = N
while n > 0:
    n -= 1
    amari = n % 26
    amari_list.append(a_list[amari])
    n = n // 26

ans = "".join(reversed(amari_list))

print(ans)
