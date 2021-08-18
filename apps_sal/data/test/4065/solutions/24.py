

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

    ans = 1
    i = 0
    while(i < n - 1):
        count = 1
        while(2 * a[i] >= a[i + 1]):
            count += 1
            i += 1
            if(i == n - 1):
                break
        ans = max(ans, count)
        i += 1
    print(ans)


if(fileoperation):
    sys.stdout = orig_stdout
    sys.stdin = orig_stdin
    inputfile.close()
    outputfile.close()
