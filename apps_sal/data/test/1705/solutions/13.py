

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
    n = int(input())
    a = list(map(int, sys.stdin.readline().split(' ')))
    one = a.count(1)
    zer = a.count(0)
    o = 0
    z = 0
    for i in range(n):
        if(a[i]):
            o += 1
        else:
            z += 1
        if(o == one):
            print(i + 1)
            break
        if(z == zer):
            print(i + 1)
            break


if(fileoperation):
    sys.stdout = orig_stdout
    sys.stdin = orig_stdin
    inputfile.close()
    outputfile.close()
