#!/usr/bin/env python3

s = [int(i) for i in input()]
ans = 0
last = 0


def check(x):
    Sum = 0
    while x != 0:
        Sum += x % 10
        x //= 10
        if Sum % 3 == 0:
            return True
    return False


for i in range(len(s)):
    if s[i] % 3 == 0:
        ans += 1
        last = 0
    else:
        last = last * 10 + s[i]
        if check(last):
            ans += 1
            last = 0
print(ans)
