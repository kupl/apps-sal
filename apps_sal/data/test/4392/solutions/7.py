t=int(input())
while t:
    n,m=map(int,input().split())
    a=input().split()
    p=input().split()
    for i in range(n):
        a[i]=int(a[i])
    visited=[0 for i in range(n)]    
    for i in range(m):
        visited[int(p[i])]=1
    ls=[]
    temp=[]
    for i in range(n):
        if(visited[i]==0):
            temp.sort()
            for j in range(len(temp)):
                ls.append(temp[j])
            temp=[a[i]]
        else:
            temp.append(a[i])
    temp.sort()
    for j in range(len(temp)):
        ls.append(temp[j])
    a.sort()
    if(a==ls):print("YES")
    else:print("NO")
    t-=1    
