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
t=int(input())
for tt in range(t):
    #n=int(input())
    n,k= map(int, sys.stdin.readline().split(' '))
    s=0
    while (n!=0):
        rem=n%k
        s+=rem
        n-=rem
        if(n>0):
            s+=1
        n//=k
    print(s)
    #a=list(map(int,sys.stdin.readline().split(' ')))
    
#####File Operations#####
if(fileoperation):
    sys.stdout = orig_stdout
    sys.stdin = orig_stdin
    inputfile.close()
    outputfile.close()
