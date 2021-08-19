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
    (a, b, c, n) = map(int, sys.stdin.readline().split(' '))
    give = (a + b + c + n) // 3
    x = give - a
    y = give - b
    z = give - c
    if give * 3 == a + b + c + n and x >= 0 and (y >= 0) and (z >= 0) and (x + y + z == n):
        print('YES')
    else:
        print('NO')
if fileoperation:
    sys.stdout = orig_stdout
    sys.stdin = orig_stdin
    inputfile.close()
    outputfile.close()
