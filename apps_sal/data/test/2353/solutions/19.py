

import sys
import math


fileoperation = 0
if(fileoperation):
    orig_stdout = sys.stdout
    orig_stdin = sys.stdin
    inputfile = open('W:/Competitive Programming/input.txt', 'r')
    outputfile = open('W:/Competitive Programming/output.txt', 'w')
    sys.stdin = inputfile
    sys.stdout = outputfile

mod = 1000000007


def nospace(l):
    ans = ''.join(str(i) for i in l)
    return ans


t = int(input())
for tt in range(t):
    a, b, c, d = map(int, sys.stdin.readline().split(' '))
    if a <= b:
        print(b)
        continue
    diff = c - d

    if diff <= 0:
        print(-1)
        continue
    else:
        rem = a - b
        slept = b
        v = (rem // diff)
        if v * diff < rem:
            v += 1
        slept += (v * c)
        print(slept)


if(fileoperation):
    sys.stdout = orig_stdout
    sys.stdin = orig_stdin
    inputfile.close()
    outputfile.close()
