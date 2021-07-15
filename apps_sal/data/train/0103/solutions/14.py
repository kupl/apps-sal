from sys import stdin
T=int(stdin.readline().strip())
for caso in range(T):
    
    n,m=list(map(int,stdin.readline().strip().split()))
    s=[list(map(int,stdin.readline().strip().split())) for i in range(n)]
    r=n
    for i in range(n):
        if 1 in s[i]:
            r-=1
    c=m
    for i in range(m):
        for j in range(n):
            if s[j][i]==1:
                c-=1
                break
    x=min(c,r)
    if x%2==0:
        print("Vivek")
    else:
        print("Ashish")
            

