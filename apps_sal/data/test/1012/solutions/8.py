# JMD
# Nagendra Jha-4096


import sys
import math

#import fractions
#import numpy

###File Operatins###
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


##### Main ####
t = int(input())
for tt in range(t):
    s = str(input())
    s = list(s)
    s.sort()
    if(s == s[::-1]):
        print(-1)
    else:
        b = ""
        for ss in s:
            b += ss
        print(b)

    #a=list(map(int,sys.stdin.readline().split(' ')))
    #n,k,s= map(int, sys.stdin.readline().split(' '))


#####File Operations#####
if(fileoperation):
    sys.stdout = orig_stdout
    sys.stdin = orig_stdin
    inputfile.close()
    outputfile.close()
