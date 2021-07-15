#!/usr/bin/env python3
n,m,k,l=list(map(int,input().split()))
q=(l+k-1)//m+1
if q*m>n:print(-1)
else:print(q)

