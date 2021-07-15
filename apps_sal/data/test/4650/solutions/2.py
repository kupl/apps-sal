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
    n=int(input())
    #n,k,s= map(int, sys.stdin.readline().split(' '))
    a=list(map(int,sys.stdin.readline().split(' ')))
    z=0
    o=0
    two=0
    for nu in a:
        if(nu%3==0):
            z+=1
        elif(nu%3==1):
            o+=1
        else:
            two+=1
    ans=min(o,two)
    o-=ans
    two-=ans
    if(o):
        ans+=o//3
    if two:
        ans+=two//3
    print(ans+z)

    
    
#####File Operations#####
if(fileoperation):
    sys.stdout = orig_stdout
    sys.stdin = orig_stdin
    inputfile.close()
    outputfile.close()
