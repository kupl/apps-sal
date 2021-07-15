D,G=map(int,input().split())
p=[0]*D
c=[0]*D
for i in range(D):
    p[i],c[i]=map(int,input().split())

ans=1000
for i in range(2 ** D):
    op = ["-"] * D
    for j in range(D):
        if ((i >> j) & 1):
            op[D - 1 - j] = "+"
    s=0
    cnt=0
    for j in range(D):
        if op[j]=="+":
            s+=100*(j+1)*p[j]
            s+=c[j]
            cnt+=p[j]
    if s<G:
        for j in range(D-1,-1,-1):
            if op[j]=="-":
                for k in range(p[j]):
                    if s>=G:
                        break
                    s+=100*(j+1)
                    cnt+=1
    ans=min(cnt,ans)

print(ans)
