from math import *


def add_bit(n, k):
    return n | 1 << k


s = input().strip()
ans = 0
if len(s) >= 5:
    ans = add_bit(ans, 0)
for i in range(len(s)):
    if s[i] >= 'a' and s[i] <= 'z':
        ans = add_bit(ans, 1)
    if s[i] >= 'A' and s[i] <= 'Z':
        ans = add_bit(ans, 2)
    if s[i] >= '0' and s[i] <= '9':
        ans = add_bit(ans, 3)
if ans == 15:
    print('Correct')
else:
    print('Too weak')
