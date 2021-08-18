

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
    n, a, x, b, y = map(int, sys.stdin.readline().split(' '))

    while 1:
        if a == x or b == y:
            break

        if a == b:
            break
        if(a < n):
            a += 1
        else:
            a = 1

        if(b > 1):
            b -= 1
        else:
            b = n
    if a == b:
        print("YES")
    else:
        print("NO")


if(fileoperation):
    sys.stdout = orig_stdout
    sys.stdin = orig_stdin
    inputfile.close()
    outputfile.close()
