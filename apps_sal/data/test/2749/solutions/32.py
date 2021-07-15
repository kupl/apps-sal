from collections import deque
h,w=map(int,input().split())
n=int(input())
a=list(map(int,input().split()))
c=1
for i in range(h):
    row=deque()
    for j in range(w):
        if i%2==0:
            row.append(c)
            a[c-1]-=1
            if a[c-1]==0:
                c+=1
        else:
            row.appendleft(c)
            a[c-1]-=1
            if a[c-1]==0:
                c+=1
    print(*row)
