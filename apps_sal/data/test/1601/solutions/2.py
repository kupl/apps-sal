from sys import stdin,stdout
n=int(stdin.readline())
l=[]
for i in range(n):
    x=list(map(int,stdin.readline().split()))
    l.append([x,i+1])
l.sort()
#print(l)
deleted=[0]*n
for i in range(n-1):
    if deleted[i]:
        continue
    if l[i][0][0]==l[i+1][0][0] and l[i][0][1]==l[i+1][0][1]:
        print(l[i][1],l[i+1][1])
        deleted[i]=deleted[i+1]=1
remaining=[]
for i in range(n):
    if deleted[i]==0:
        remaining.append(l[i])
del deleted
n=len(remaining)
deleted=[0]*n
for i in range(n-1):
    if deleted[i]:
        continue
    if remaining[i][0][0]==remaining[i+1][0][0]:
        print(remaining[i][1],remaining[i+1][1])
        deleted[i]=deleted[i+1]=1
last=[]
for i in range(n):
    if deleted[i]==0:
        last.append(remaining[i])
for i in range(0,len(last),2):
    print(last[i][1],last[i+1][1])

