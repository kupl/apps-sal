#JMD
#Nagendra Jha-4096
import sys
import bisect

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

def search(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect.bisect_right(a, x)
    if(i==0):
        return -1
    return i-1



##### Main ####
n=int(input())
a=list(map(int, sys.stdin.readline().split(' ')))
x,f=map(int, sys.stdin.readline().split(' '))

ans=0

for aa in a:
    if(aa<=x):
        continue
    val=(aa-x)//(x+f)
    if(val*(x+f)<aa-x):
        val+=1
    ans+=val
print(f*ans)
    

    
#####File Operations#####
if(fileoperation):
    sys.stdout = orig_stdout
    sys.stdin = orig_stdin
    inputfile.close()
    outputfile.close()
