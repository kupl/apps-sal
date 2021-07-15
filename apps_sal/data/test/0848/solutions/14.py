import sys,math
n,k=list(map(int,sys.stdin.readline().split()))
if n<=2*k:
    print(-1)
else:
    ans=[]
    for i in range(n):
        
        for j in range(i+1,k+i+1):
            if j+1==n:
                ans.append([i+1,j+1])
            else:
                ans.append([i+1,((j+1)%n)])
    print(len(ans))
    for i in range(len(ans)):
        print(*ans[i])

