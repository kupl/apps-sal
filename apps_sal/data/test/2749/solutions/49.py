from collections import deque
H,W=map(int,input().split())
N=int(input())
a=list(map(int,input().split()))

#print(a)
j=1
for i in range(H):
    x=deque()
    while len(x)<W:
        if i%2==0:
            a[j-1]-=1
            x.append(str(j))
        else:
            a[j-1]-=1
            x.appendleft(str(j))
        if a[j-1]==0:
            j+=1
    A=" ".join(list(x))
    print(A)
