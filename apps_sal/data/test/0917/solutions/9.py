import sys
import math
fileoperation = 0
if fileoperation:
    orig_stdout = sys.stdout
    orig_stdin = sys.stdin
    inputfile = open('W:/Competitive Programming/input.txt', 'r')
    outputfile = open('C:/Users/njhab/Desktop/output.txt', 'w')
    sys.stdin = inputfile
    sys.stdout = outputfile
mod = 1000000007


def nospace(l):
    ans = ''.join((str(i) for i in l))
    return ans


t = 1
for tt in range(t):
    (n, h, m) = map(int, sys.stdin.readline().split(' '))
    a = []
    for i in range(n):
        a.append(h)
    for i in range(m):
        (l, r, x) = map(int, sys.stdin.readline().split(' '))
        for j in range(l - 1, r):
            a[j] = min(a[j], x)
    ans = 0
    for aa in a:
        ans += aa * aa
    print(ans)
if fileoperation:
    sys.stdout = orig_stdout
    sys.stdin = orig_stdin
    inputfile.close()
    outputfile.close()
