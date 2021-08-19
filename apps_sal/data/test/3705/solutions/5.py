#!/usr/bin/env python3
n = int(input())
s = input()
a = s.count('8')
b = n - a
cnt = 0
while a >= 1 and a + b >= 11:
    a -= 1
    b -= 10
    if b < 0:
        a += b
        b = 0
    cnt += 1
print(cnt)
