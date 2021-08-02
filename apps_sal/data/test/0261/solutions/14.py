import sys
import os
import fileinput
n = int(input())
s = input().strip()

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j - 1 >= n or j - 1 + i >= n or j - 1 + 2 * i >= n or j - 1 + 3 * i >= n or j - 1 + 4 * i >= n:
            break
        t = "%s%s%s%s%s" % (s[j - 1], s[j - 1 + i], s[j - 1 + 2 * i], s[j - 1 + 3 * i], s[j - 1 + 4 * i])
        if t == "*****":
            print("yes")
            return

print("no")
