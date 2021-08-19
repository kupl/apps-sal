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
    (x, n, m) = map(int, sys.stdin.readline().split(' '))
    while x > 20 and n > 0:
        x = x // 2
        x += 10
        n -= 1
    while x > 0 and m > 0:
        x -= 10
        m -= 1
    if x <= 0:
        print('YES')
    else:
        print('NO')
if fileoperation:
    sys.stdout = orig_stdout
    sys.stdin = orig_stdin
    inputfile.close()
    outputfile.close()
