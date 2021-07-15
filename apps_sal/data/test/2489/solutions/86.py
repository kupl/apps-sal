import sys
input = sys.stdin.readline

#n = int(input())
#l = list(map(int, input().split()))

'''
a=[]
b=[]
for i in range():
    A, B = map(int, input().split())
    a.append(A)   
    b.append(B)'''
def cal(n,li):
    lis=[True]*(n+1)
    for item in li:
        if lis[item]:
            for i in range(item*2,n+1,item):
                lis[i]=False
    return lis
from collections import Counter

n=int(input())
a=list(map(int,input().split()))
a.sort()
l=cal(a[-1],a)
ll=Counter(a)
#print(l,ll)
ans=0
for i in range(n):
    if ll[a[i]]==1:
        if l[a[i]]:
            ans+=1

print(ans)

