

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


n, m = map(int, sys.stdin.readline().split(' '))
c = list(map(int, sys.stdin.readline().split(' ')))
a = list(map(int, sys.stdin.readline().split(' ')))
ans = 0

for i in range(n):
    if(len(a) and c[i] <= a[0]):
        del(a[0])
        ans += 1
print(ans)


if(fileoperation):
    sys.stdout = orig_stdout
    sys.stdin = orig_stdin
    inputfile.close()
    outputfile.close()
