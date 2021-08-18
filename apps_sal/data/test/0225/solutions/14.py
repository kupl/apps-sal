

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


t = 1
for tt in range(t):
    a, b, c, d = map(int, sys.stdin.readline().split(' '))

    s = (a + b + c + d)

    if (s % 2) == 0:
        v = s // 2

        if a == v or b == v or c == v or d == v:
            print("YES")
        elif (a + b) == v or (a + c) == v or (a + d) == v:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")


if(fileoperation):
    sys.stdout = orig_stdout
    sys.stdin = orig_stdin
    inputfile.close()
    outputfile.close()
