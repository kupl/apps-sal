# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 20:14:03 2019

@author: Tejasvi Sharma
"""

k1,k2,k3 = list(map(int,input().split(" ")))
n = k1+k2+k3
a = list(map(int,input().split(" ")))
b = list(map(int,input().split(" ")))
c = list(map(int,input().split(" ")))

B = list(range(k1+k2+k3))

for i in a:
    B[i-1]=1
for i in b:
    B[i-1]=2
for i in c:
    B[i-1]=3

p1,p2,p3 = (0,0,0)

inf = int(2*1e5+3)
stateStorage = [[inf for i in range(3)] for j in range(2)]

for i in range(3):
    stateStorage[n%2][i]=0
    

def fillMatrix(n):
    for i in range(n-1,-1,-1):
        stateStorage[i%2][0] = (1-int(B[i]==1)) + min(stateStorage[(i+1)%2][0], stateStorage[(i+1)%2][1], stateStorage[(i+1)%2][2])
        stateStorage[i%2][1] = (1-int(B[i]==2)) + min(stateStorage[(i+1)%2][2], stateStorage[(i+1)%2][1])
        stateStorage[i%2][2] = (1-int(B[i]==3)) + stateStorage[(i+1)%2][2]
#        print(str(i)+"->")
#        print(stateStorage[i%2][0],stateStorage[i%2][1],stateStorage[i%2][2])
    return min(stateStorage[0][0],stateStorage[0][1],stateStorage[0][2])
        

#def recF(index, state):
#    if stateStorage[index][state-1]!=inf:
#        return stateStorage[index][state-1]
#    val = 0
#    if state==1:
#        if B[index]==1:
#            val += recF(index+1, state)
#        elif B[index]==2:
#            val += min(recF(index+1,state)+1, recF(index+1,state=2))
#        else:
#            val += min(recF(index+1,state)+1, recF(index+1,state=3))
#    elif state==2:
#        if B[index]==1:
#            val += recF(index+1, state)+1
#        elif B[index]==2:
#            val += recF(index+1, state)
#        else:
#            val += min(recF(index+1,state)+1, recF(index+1,state=3))
#    elif state==3:
#        if B[index]==3:
#            val += recF(index+1, state)
#        else:
#            val += recF(index+1, state)+1
#            
#    stateStorage[index][state-1]=val
#    return stateStorage[index][state-1]

        
ans = fillMatrix(n)
print(ans)

