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
t = int(input())
a = list(map(int, sys.stdin.readline().split(' ')))
s = set(a)
ans = len(s)
if(0 in s):
    ans -= 1
print(ans)


#####File Operations#####
if(fileoperation):
    sys.stdout = orig_stdout
    sys.stdin = orig_stdin
    inputfile.close()
    outputfile.close()
