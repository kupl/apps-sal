from collections import deque

n=int(input())
s=[int(x) for x in input().split()]
b=[]
mx=-1
for i in range(0,len(s)):
    t=bin(s[i])
    t=t[2:]
    b.append(t)
    mx=max(mx,len(t))

for i in range(0,len(b)):
    b[i]='0'*(mx-len(b[i]))+b[i]

flag=0
L=[]
kk=dict()
for i in range(0,mx):
    c=0
    h=[]
    for j in range(0,len(b)):
        if(b[j][i]=='1'):
            c+=1
            h.append(j)
    if(len(h)==2 and kk.get(tuple(h))==None):
        h=tuple(h)
        L.append(h)
        kk[h]=1
    if(c>2):
        flag=1
        break
#print(L)

if(flag==1):
    print(3)
else:
    temp=1000000007
    for i in range(0,len(L)):

        arr=[]
        for j in range(n):
            s1=[]
            arr.append(s1)

        for j in range(0,len(L)):
            if(j==i):
                src=L[j][0]
                dst=L[j][1]

            else:
                arr[L[j][0]].append(L[j][1])
                arr[L[j][1]].append(L[j][0])

        q=deque()
        q.append((src,0))
        visited=[False]*n
        visited[src]=True

        while(q):

            r=q.popleft()

            visited[r[0]]=True
            if(r[0]==dst):
                temp=min(temp,r[1]+1)
                break

            for j in arr[r[0]]:
                if(visited[j]==False):
                    q.append((j,r[1]+1))


    if(temp==1000000007):
        print(-1)
    else:
        print(temp)

        

        
                
    

