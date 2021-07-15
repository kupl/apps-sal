h,w=map(int,input().split())
n=int(input())
a=list(map(int,input().split()))

ans=[[0]*w for _ in range(h)]
i=0
j=0
jugh=0


if w==1:
    for i in range(n):
        for j in range(a[i]):
            print(i+1)
    return



for z in range(n):
    count=0
    while count<a[z]:
       # print(i,j,z+1)
        if jugh==0:
            ans[i][j]=z+1
            j+=1
            c=0
        elif jugh==2:
            if j==0:
                jugh=0
                c=1
                ans[i][j]=z+1
                j+=1
            else:
                
                jugh=1
                c=1
                
                ans[i][j]=z+1
                j-=1
        else:
            ans[i][j]=z+1
            j-=1
            c=0

        if j==w and c==0:
            i+=1
            j-=1
            jugh=2
        if j==-1 and c==0:
            i+=1
            j+=1
            jugh=2
            
        count+=1

for i in range(h):
    for j in range(w):
        print(ans[i][j],end=" ")
    print()

