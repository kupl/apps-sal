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
    (b, k) = map(int, sys.stdin.readline().split(' '))
    ans = 0
    a = list(map(int, sys.stdin.readline().split(' ')))
    a = a[::-1]
    for i in range(k):
        v = pow(b, i, 2)
        ans += v * a[i]
        ans %= 2
    if ans:
        print('odd')
    else:
        print('even')
if fileoperation:
    sys.stdout = orig_stdout
    sys.stdin = orig_stdin
    inputfile.close()
    outputfile.close()
