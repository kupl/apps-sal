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
t = int(input())
for tt in range(t):
    # n=int(input())
    a, b = map(int, sys.stdin.readline().split(' '))

    if(a == b):
        print(0)
    elif(a > b):
        if((a - b) % 2 == 0):
            print(1)
        else:
            print(2)
    else:
        if((a - b) % 2):
            print(1)
        else:
            print(2)
    #a=list(map(int,sys.stdin.readline().split(' ')))


#####File Operations#####
if(fileoperation):
    sys.stdout = orig_stdout
    sys.stdin = orig_stdin
    inputfile.close()
    outputfile.close()
