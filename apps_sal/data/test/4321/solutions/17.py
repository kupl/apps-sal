#JMD
#Nagendra Jha-4096

#a=list(map(int,sys.stdin.readline().split(' ')))
#n,k,s= map(int, sys.stdin.readline().split(' '))

import sys
import math

#import fractions
#import numpy

###Defines...###
mod=1000000007

###FUF's...###
def nospace(l):
	ans=''.join(str(i) for i in l)
	return ans



##### Main ####
n,k= list(map(int, sys.stdin.readline().split(' ')))
for i in range(k):
    if(n%10):
        n-=1
    else:
        n=n//10
print(n)

