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
    (n, k) = list(map(int, sys.stdin.readline().split(' ')))
    a = list(map(int, sys.stdin.readline().split(' ')))
    a.sort()
    ans = 0
    c = 1
    for i in range(n):
        if c > a[n - 1] or c > a[i]:
            ans += a[i] - 1
            continue
        if i != n - 1:
            ans += a[i] - 1
            c += 1
        else:
            ans += c - 1
    print(ans)
if fileoperation:
    sys.stdout = orig_stdout
    sys.stdin = orig_stdin
    inputfile.close()
    outputfile.close()
