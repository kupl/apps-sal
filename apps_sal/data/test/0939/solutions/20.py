n,m=map(int,input().split())
l=[0]*(n+1)
for i in range(m):
    a,b,c=map(int,input().split())
    if(l[a]!=0):
        if(l[a]==1):
            l[b]=2
            l[c]=3
        elif(l[a]==2):
            l[b]=3
            l[c]=1
        else:
            l[b]=1
            l[c]=2
    elif(l[b]!=0):
        if(l[b]==1):
            l[c]=2
            l[a]=3
        elif(l[b]==2):
            l[c]=3
            l[a]=1
        else:
            l[c]=1
            l[a]=2
    elif(l[c]!=0):
        if(l[c]==1):
            l[a]=2
            l[b]=3
        elif(l[c]==2):
            l[a]=3
            l[b]=1
        else:
            l[a]=1
            l[b]=2
    else:
        l[a]=1
        l[b]=2
        l[c]=3
for i in range(1,n+1):
    print(l[i],end=' ')

