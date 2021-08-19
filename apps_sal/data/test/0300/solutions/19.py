# JMD
# Nagendra Jha-4096

#a=list(map(int,sys.stdin.readline().split(' ')))
#n,k,s= map(int, sys.stdin.readline().split(' '))

import sys
import math

#import fractions
#import numpy

###File Operations###
fileoperation = 0
if(fileoperation):
    orig_stdout = sys.stdout
    orig_stdin = sys.stdin
    inputfile = open('W:/Competitive Programming/input.txt', 'r')
    outputfile = open('W:/Competitive Programming/output.txt', 'w')
    sys.stdin = inputfile
    sys.stdout = outputfile

###Defines...###
mod = 1000000007

###FUF's...###


def nospace(l):
    ans = ''.join(str(i) for i in l)
    return ans


##### Main ####
n = int(input())
a = list(map(int, sys.stdin.readline().split(' ')))
reach = math.ceil(4.5 * n)
s = sum(a)
a.sort()
ans = reach - s
count = 0
for aa in a:
    if(ans <= 0):
        break
    ans -= (5 - aa)
    count += 1
print(count)
#####File Operations#####
if(fileoperation):
    sys.stdout = orig_stdout
    sys.stdin = orig_stdin
    inputfile.close()
    outputfile.close()
