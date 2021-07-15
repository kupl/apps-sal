h,w=map(int,input().split())
n=int(input())
a=list(map(int,input().split()))
ans=[[0 for i in range(w)] for j in range(h) ]

v=0
d=0
df=0
for i in range(n):
    t=i+1
    f=0
    while f<a[i]:
        if df==0:
            ans[v][d]=t

        elif df==1:

            ans[v][w-1-d]=t
        f+=1
        d+=1
        if df==0 and d==w:
            v+=1
            df^=1
            d=0
        if df==1 and w-d==0:
            v += 1
            df ^= 1
            d = 0
for h in ans:
    print(*h)
