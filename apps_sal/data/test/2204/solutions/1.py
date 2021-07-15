import sys,heapq

input=sys.stdin.readline

for _ in range(int(input())):
    if _!=0:
        s=input()
    n,m=list(map(int,input().split()))
    flower=[]#b,a
    for i in range(m):
        a,b=list(map(int,input().split()))
        flower.append((b,a))
    flower.sort()
    S=0
    N=0
    ans=-1
    que=[]
    if n==1:
        ans=max(flower[i][1] for i in range(m))
        print(ans)
        continue
    for i in range(m):
        b,a=flower[i]
        while que and b>que[0]:
            A=heapq.heappop(que)
            S-=A
            N-=1
        temp=b*(n-1-N)+a+S
        ans=max(temp,ans)
        if N==n-1:
            if que[0]<a:
                S-=que[0]
                heapq.heappop(que)
                S+=a
                heapq.heappush(que,a)
        else:
            heapq.heappush(que,a)
            S+=a
            N+=1

    print(ans)

