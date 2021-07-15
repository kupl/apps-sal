from sys import stdin
q=int(stdin.readline().strip())
for i in range(q):
    c,m,x=list(map(int,stdin.readline().strip().split()))
    n=c+m+x
    y=min(c,m)
    t=n//3
    ans=min(y,t)
    print(ans)

