

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


n, m, a, b = map(int, sys.stdin.readline().split(' '))
val = (m - (n % m)) * a
v2 = (n % m) * b
print(min(val, v2))


if(fileoperation):
    sys.stdout = orig_stdout
    sys.stdin = orig_stdin
    inputfile.close()
    outputfile.close()
