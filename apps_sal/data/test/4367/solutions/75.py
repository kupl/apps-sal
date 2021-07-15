#!/usr/bin/env python3
n,r=list(map(int,input().split()))
ans=r
if n>=10:
    print(r)
else:
    print((r+100*(10-n)))

