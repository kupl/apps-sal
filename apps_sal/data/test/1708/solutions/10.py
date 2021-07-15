# cook your dish here
n,m=map(int,input().split())
a=list(map(int,input().split()))
c=list(map(int,input().split()))
cl=[]
for i in range(n):
    cl.append([c[i],i])
#print(cl)
def fun(itm):
    return itm[0]
cl.sort(key=fun)
idx=0
for i in range(m):
    x,y=map(int,input().split())
    x-=1
    cost=0
    if(a[x]>=y):
        a[x]-=y
        cost+=c[x]*y
        y=0
    else:
        cost+=c[x]*a[x]
        y-=a[x]
        a[x]=0
        flag=0
        while(idx<n and y>0):
            if(a[cl[idx][1]]>=y):
                a[cl[idx][1]]-=y
                cost+=cl[idx][0]*y
                y=0
                flag=1
            else:
                cost+=cl[idx][0]*a[cl[idx][1]]
                y-=a[cl[idx][1]]
                a[cl[idx][1]]=0
                idx+=1
        if(flag==0):
            cost=0
    print(cost)
