import os, sys, re, math

S = input()
Q = int(input())

direction = 1
prefix = ''
suffix = ''
for i in range(Q):
    query = input().split()
    if int(query[0]) == 1:
        direction = 2 if direction == 1 else 1
    else:
        if int(query[1]) ^ direction == 0:
            prefix = query[2] + prefix
        else:
            suffix = suffix + query[2]

S = prefix + S + suffix
if direction == 1:
    print(S)
else:
    print((S[::-1]))

