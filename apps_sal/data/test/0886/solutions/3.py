import sys
import math

s = input()
s = list(s)

for i in range(len(s)):
    if int(s[i]) % 2 == 0 and s[i] < s[-1]:
        s[i], s[-1] = s[-1], s[i]
        print("".join(s))
        return

for i in range(len(s) - 1, -1, -1):
    if int(s[i]) % 2 == 0:
        s[i], s[-1] = s[-1], s[i]
        print("".join(s))
        return

print(-1)
