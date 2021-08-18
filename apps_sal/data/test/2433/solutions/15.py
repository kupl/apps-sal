

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
    b, p, f = map(int, sys.stdin.readline().split(' '))
    h, c = map(int, sys.stdin.readline().split(' '))
    b = b // 2

    ans = 0
    if h >= c:
        val = min(b, p)
        ans += val * h
        b -= val

        val = min(b, f)
        ans += val * c
    else:
        val = min(b, f)
        ans += val * c
        b -= val
        val = min(b, p)
        ans += val * h

    print(ans)


if(fileoperation):
    sys.stdout = orig_stdout
    sys.stdin = orig_stdin
    inputfile.close()
    outputfile.close()
