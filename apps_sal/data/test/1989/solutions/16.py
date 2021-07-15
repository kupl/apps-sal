#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sem título.py
#  
#  Copyright 2020 Alencar <Alencar@ALENCAR-PC>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  



n=int(input())
def getsum(BITTree,i): 
    s = 0
    i = i+1
    while i > 0: 
        s += BITTree[i] 
        i -= i & (-i) 
    return s  
def updatebit(BITTree , n , i ,v): 
    i += 1
    while i <= n: 
        BITTree[i] += v 
        i += i & (-i) 
a=list(map(int,input().split()))
pre=dict()
pos=dict()
for i in range(n):
    if(pre.get(a[i],None)==None):
        pre[a[i]]=0
    pre[a[i]]+=1 
ans=0
BIT=[0]*(n+1)
for i in range(n-1,0,-1):
    pre[a[i]]-=1 
    if(pos.get(a[i],None)==None):
        pos[a[i]]=0
    pos[a[i]]+=1 
    updatebit(BIT,n,pos[a[i]],1)
    temp=getsum(BIT,pre[a[i-1]]-1)
    ans+=temp
print(ans)


