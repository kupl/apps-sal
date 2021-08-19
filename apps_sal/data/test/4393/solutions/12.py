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


t = 1
for tt in range(t):
    n = int(input())
    s = str(input())
    c = 1
    i = 0
    ans = ''
    while i < n:
        ans += s[i]
        i += c
        c += 1
    print(ans)
if fileoperation:
    sys.stdout = orig_stdout
    sys.stdin = orig_stdin
    inputfile.close()
    outputfile.close()
