import sys
import math
fileoperation = 0
if fileoperation:
    orig_stdout = sys.stdout
    orig_stdin = sys.stdin
    inputfile = open('W:/Competitive Programming/input.txt', 'r')
    outputfile = open('W:/Competitive Programming/output.txt', 'w')
    sys.stdin = inputfile
    sys.stdout = outputfile
mod = 1000000007


def nospace(l):
    ans = ''.join((str(i) for i in l))
    return ans


t = int(input())
for tt in range(t):
    n = int(input())
    s = str(input())
    if n > 2:
        print('YES')
        print(2)
        print(s[0], s[1:])
    elif int(s[0]) < int(s[1]):
        print('YES')
        print(2)
        print(s[0], s[1:])
    else:
        print('NO')
if fileoperation:
    sys.stdout = orig_stdout
    sys.stdin = orig_stdin
    inputfile.close()
    outputfile.close()
