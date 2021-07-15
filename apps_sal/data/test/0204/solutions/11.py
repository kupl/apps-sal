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
    #a=list(map(int,sys.stdin.readline().split(' ')))
    a,b,x,y= map(int, sys.stdin.readline().split(' '))
    g=math.gcd(x,y)
    x=x//g
    y=y//g

    print(min(a//x,b//y))
    
#####File Operations#####
if(fileoperation):
    sys.stdout = orig_stdout
    sys.stdin = orig_stdin
    inputfile.close()
    outputfile.close()
