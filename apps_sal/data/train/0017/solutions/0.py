class BIT():
    def __init__(self,n):
        self.BIT=[0]*(n+1)
        self.num=n

    def query(self,idx):
        res_sum = 0
        while idx > 0:
            res_sum += self.BIT[idx]
            idx -= idx&(-idx)
        return res_sum

    #Ai += x O(logN)
    def update(self,idx,x):
        while idx <= self.num:
            self.BIT[idx] += x
            idx += idx&(-idx)
        return

import sys,random

input=sys.stdin.readline

for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    pair=[[] for i in range(n+1)]
    for i in range(n):
        for j in range(i+1,n):
            if a[i]==a[j]:
                pair[i+1].append(j+1)

    bit=BIT(n)
    ans=0
    for i in range(1,n+1):
        minus=bit.query(i)
        for r in pair[i]:
            ans+=bit.query(r-1)-minus
        for r in pair[i]:
            bit.update(r,1)

    print(ans)
    

