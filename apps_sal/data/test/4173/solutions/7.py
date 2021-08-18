

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
    n, a, b = map(int, sys.stdin.readline().split(' '))
    a1 = n * a
    a2 = (n // 2) * b
    if(n % 2):
        a2 += a
    print(min(a1, a2))


if(fileoperation):
    sys.stdout = orig_stdout
    sys.stdin = orig_stdin
    inputfile.close()
    outputfile.close()
