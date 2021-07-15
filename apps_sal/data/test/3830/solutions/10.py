
from sys import stdin
import sys

tt = int(stdin.readline())

for loop in range(tt):

    n = int(stdin.readline())
    s = stdin.readline()[:-1]

    if ("<" not in s) or (">" not in s):
        print (n)
        continue

    ans = 0
    for i in range(n):
        if s[(i-1)%n] == "-" or s[i] == "-":
            ans += 1

    print (ans)

