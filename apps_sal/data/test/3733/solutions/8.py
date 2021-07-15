from sys import stdin
input=stdin.readline
n,I=map(int,input().split())
a=sorted(list(map(int,input().split())))
key=[]
k=min(I*8//n,20)
K=min(2**k,n)
last=-1
for i in range(n):
    if a[i]==last:
        key[-1]+=1
    else:
        key.append(1)
        last=a[i]
now=0
best=0
for i in range(len(key)):
    if i<K:
        now+=key[i]
    else:
        now+=key[i]
        now-=key[i-K]
    best=max(now,best)
print(n-best)
