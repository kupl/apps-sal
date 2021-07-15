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
    #a=list(map(int,sys.stdin.readline().split(' ')))
    n,k= list(map(int, sys.stdin.readline().split(' ')))
    a=list(map(int,sys.stdin.readline().split(' ')))
    a.sort()

    ans=0
    c=1

    for i in range(n):
    	if(c>a[n-1] or c>a[i]):
    		ans+=a[i]-1
    		continue
    	if(i!=n-1):
    		ans+=a[i]-1
    		c+=1
    	else:
    		ans+=c-1
    print(ans)


    
    
#####File Operations#####
if(fileoperation):
    sys.stdout = orig_stdout
    sys.stdin = orig_stdin
    inputfile.close()
    outputfile.close()

