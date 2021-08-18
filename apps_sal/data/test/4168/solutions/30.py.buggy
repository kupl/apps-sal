#!/usr/bin/env python3

n = int(input())

if n == 0:
    print((0))
    return
ans = []
while(n != 0):

    rem = n % 2

    n = (n - rem) // (-2)

    ans.append(rem)

ans.reverse()

print(("".join(map(str, ans))))
