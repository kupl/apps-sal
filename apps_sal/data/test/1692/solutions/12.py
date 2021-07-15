#!/usr/bin/env python
s = list(map(int, list(input())))
a = 0
while len(s) > 0:
    if(not ((10 * s[len(s) - 2] + s[len(s) - 1]) % 4)):
        a += len(s) - 1
    if s[len(s) - 1] == 4 or s[len(s) - 1] == 8 or s[len(s) - 1] == 0:
        a += 1
    s.pop()
print(a)

