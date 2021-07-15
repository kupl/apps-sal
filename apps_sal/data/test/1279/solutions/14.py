#JMD
#Nagendra Jha-4096

 
import sys
import math

#import fractions
#import numpy
 
###File Operations###
fileoperation=0
if(fileoperation):
    orig_stdout = sys.stdout
    orig_stdin = sys.stdin
    inputfile = open('W:/Competitive Programming/input.txt', 'r')
    outputfile = open('W:/Competitive Programming/output.txt', 'w')
    sys.stdin = inputfile
    sys.stdout = outputfile

###Defines...###
mod=1000000007
 
###FUF's...###
def nospace(l):
    ans=''.join(str(i) for i in l)
    return ans
 
 
 
##### Main ####
t=1
for tt in range(t):
    #n=int(input())
    n,m= map(int, sys.stdin.readline().split(' '))
    a=list(map(int,sys.stdin.readline().split(' ')))
    b=list(map(int,sys.stdin.readline().split(' ')))
    ae=0
    ao=0
    be=0
    bo=0
    for i in range(m):
        if(b[i]%2):
            bo+=1
        else:
            be+=1
    for i in range(n):
        if(a[i]%2):
            ao+=1
        else:
            ae+=1
    print(min(ao,be)+min(ae,bo)) 
    
#####File Operations#####
if(fileoperation):
    sys.stdout = orig_stdout
    sys.stdin = orig_stdin
    inputfile.close()
    outputfile.close()
