#!/usr/bin/env python3
def s(x):
    return sum(map(int, str(x)))
n = int(input())
ans = 0
a = 0
while a <= n:
    b = n - a
    ans = max(ans, s(a) + s(b))
    a = 10 * a + 9
print(ans)

