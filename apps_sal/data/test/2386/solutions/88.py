# coding: utf-8
n = int(input())
A = list(map(int,input().split()))
L=[]
for i in range(n):
    L.append(A[i]-(i+1))
L.sort()
#print(L)
if n==1:
    b1=L[0]
    b2=L[0]
elif n==2:
    b1=L[0]
    b2=L[1]
else:
    b1=L[n//2]
    b2=L[n//2-1]
ans=0
cnt1=0
cnt2=0
for i in range(n):
    cnt1+=abs(L[i]-b1)
    cnt2+=abs(L[i]-b2)
print(min(cnt1,cnt2))
