n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
j=0
mk=a[0]
i=0
while(i!=m):
    if b[i]>mk:
        j+=1
        mk+=a[j]
    else:
        print(j+1,a[j]-(mk-b[i]))
        i+=1
