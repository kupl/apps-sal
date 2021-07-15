
def process(n,x,y):
    x,y=min(x,y),max(x,y)
    print()
    for i1 in reversed(range(1,n)):
        if((y-x)%i1==0):
            c=0
            flag=0
            i=((y-x)//i1)
            while(n>0):
                t=(y-c*i)
                if(t<=0 and flag==0):
                    flag=1
                    c=1
                if(flag==0):
                    print(t,end=" ")
                else:
                    print(y+c*i,end=" ")
                n-=1
                c+=1
            return



tests=int(input())
for i in range(tests):
    n,x,y=list(map(int,input().split()))
    process(n,x,y)
