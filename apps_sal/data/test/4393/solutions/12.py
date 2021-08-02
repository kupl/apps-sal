# JMD
# Nagendra Jha-4096


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
t = 1
for tt in range(t):
    n = int(input())
    s = str(input())
    c = 1
    i = 0
    ans = ""
    while(i < n):
        ans += s[i]
        i += c
        c += 1
    print(ans)
    #a=list(map(int,sys.stdin.readline().split(' ')))
    #n,k,s= map(int, sys.stdin.readline().split(' '))


#####File Operations#####
if(fileoperation):
    sys.stdout = orig_stdout
    sys.stdin = orig_stdin
    inputfile.close()
    outputfile.close()
