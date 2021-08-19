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
    a = list(map(int, sys.stdin.readline().split(' ')))
    b = 2 * a
    ans = 0
    curr = 0
    for i in range(len(b)):
        if b[i] == 1:
            curr += 1
        else:
            ans = max(ans, curr)
            curr = 0
    print(ans)
if fileoperation:
    sys.stdout = orig_stdout
    sys.stdin = orig_stdin
    inputfile.close()
    outputfile.close()
