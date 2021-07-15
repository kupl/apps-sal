H,W=map(int,input().split())
N=int(input())
a=list(map(int,input().split()))

ans=[[0]*W for _ in range(H)]
p=[0,0]
for i in range(N):
    cnt=a[i]
    while cnt>0:
        ans[p[0]][p[1]]=i+1
        if p[1]%2==0:
            if p[0]==H-1:
                p[1]+=1
            else:
                p[0]+=1
        else:
            if p[0]==0:
                p[1]+=1
            else:
                p[0]-=1
        cnt-=1

for i in range(H):
    print(*ans[i])
