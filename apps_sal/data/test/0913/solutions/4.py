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
    n=int(input())
    #n,k,s= map(int, sys.stdin.readline().split(' '))
    a=list(map(int,sys.stdin.readline().split(' ')))
    b=list(map(int,sys.stdin.readline().split(' ')))

    c=0
    d=0

    for i in range(n):
        if(a[i]!=b[i]):
            if(a[i]==1):
                c+=1
            else:
                d+=1
    if c==0:
        print(-1)
        continue
    v=(d+1)//c
    if(v*c<d+1):
        print(v+1)
    else:
        print(v)
    
    
#####File Operations#####
if(fileoperation):
    sys.stdout = orig_stdout
    sys.stdin = orig_stdin
    inputfile.close()
    outputfile.close()
