# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 00:37:04 2016

@author: Arpan
"""

n=int(input())

class req:
    def __init__(self,no,size,cash):
        self.no=no
        self.size=size
        self.cash=cash
class table:
    def __init__(self,no,size):
        self.no=no
        self.size=size
    
rl=[]   
    
for i in range(n):
    s,c=[int(x) for x in input().split()]    
    a=req(i+1,s,c)
    rl.append(a)
k=int(input())
t=[int(x) for x in input().split()]

tl=[]

for i in range(len(t)):
    a=table(i+1,t[i])
    tl.append(a)


rl.sort(key=lambda x: x.cash,reverse=True)
tl.sort(key=lambda x: x.size)

tot=0
seated=0
a=[]

for i in tl:
    s=i.size
    for j in rl:
        if j.size<=i.size:
            tot+=j.cash
            seated+=1
            a.append([j.no,i.no])
            rl.remove(j)
            break
a.sort(key=lambda x: x[0])
print(seated,tot)
for i in a:
    print(i[0],i[1])
            


