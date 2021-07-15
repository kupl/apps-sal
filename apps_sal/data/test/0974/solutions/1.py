from collections import deque
n=int(input())
s=0
c=1
q=deque([])
l=False
for i in range(2*n):
    t=input()
    if t[0]=='a':
        m=int(t[4:])
        q.append(m)
        l=False
    else:
        if len(q)>0:
            f=q.pop()
            if l==False and f!=c:
                s+=1
                l=True
                q=[]
        c+=1
print(s)
