#!/usr/bin/env python3
n=int(input())
w=list(map(int,input().split()))
ans=1100000
for i in range(n):
    ans=min(ans,abs(sum(w[0:i])-sum(w[i:n])))
print(ans)
