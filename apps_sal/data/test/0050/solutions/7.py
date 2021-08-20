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
    (n, m, r) = map(int, sys.stdin.readline().split(' '))
    a = list(map(int, sys.stdin.readline().split(' ')))
    b = list(map(int, sys.stdin.readline().split(' ')))
    rem = r % min(a)
    print(max(r, max(b) * (r // min(a)) + rem))
if fileoperation:
    sys.stdout = orig_stdout
    sys.stdin = orig_stdin
    inputfile.close()
    outputfile.close()
