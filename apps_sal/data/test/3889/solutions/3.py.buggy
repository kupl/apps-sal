#!/bin/python3
import sys
n = input()
a = input()

count = [0] * 26

diff = set(a)

for c in a:
    count[ord(c) - ord('a')] += 1

if len(diff) == 1:
    print("Yes")
else:
    for c in count:
        if c >= 2:
            print("Yes")
            return
    print("No")
