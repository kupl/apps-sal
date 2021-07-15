'''
Created on Jul 29, 2016

@author: Md. Rezwanul Haque
'''
#from pip.util import Inf
#import math
''''
n = int(input())
L = list(map(int,input().split()))
cnt  = 0
for i in range(n):
    for j in range(i,n):
        if i<j and (L[i]+L[j])%2 == 0:
            for k in range(31):
                if pow(2, k) == L[i]+L[j]:
                    cnt+=1
                    #print(i,j)
                    break
            
            #cnt+=1
print(cnt)'''


n = int(input())

d = {}

for i in input().split():
    if int(i) in d:
        d[int(i)]+=1
    else:
        d[int(i)] = 1
        
#print(d)
L = []

for i in range(1,33):
    L.append(2**i)
    
ans = 0

for i in d:
    for j in L:
        if j-i in d:
            if j-i!= i:
                #print(d[j-i],d[i])
                ans+=d[j-i]*d[i]
            else:
                #print(d[i]-1,d[i])
                ans+=(d[i]-1)*(d[i])
#print(ans)
print(ans//2)


