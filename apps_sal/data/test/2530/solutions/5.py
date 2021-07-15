# cook your dish here
n,m=map(int,input().split())
l,d,k={},{},{}
for i in range(n):
    a,b=input().split()
    k[a]=b
    l[a]=0
    d[b]=0
for u in range(m):
    s=input()
    l[s]+=1
    d[k[s]]+=1
x=0
r=''
for i in d:
    if(d[i]==x):
        if(i<r):
            r=i
    elif(d[i]>x):
        x=d[i]
        r=i
x=0
rr=''
for i in l:
    if(l[i]==x):
        if(i<rr):
            rr=i
    elif(l[i]>x):
        x=l[i]
        rr=i
print(r)
print(rr)

