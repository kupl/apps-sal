N, M=map(int,input().split())
s=list()
c=list()
a=0
for i in range(0,M):
    s.append(0)
    c.append(0)
for i in range(0,M):
    s[i], c[i]=map(int,input().split())
for i in range(0,M):
    for j in range(0,M):
        if s[i]==s[j] and c[i]!=c[j]:
            print("-1")
            break
    else:
        continue
    break
else:
    if N==1:
        b=[0]
        for i in range(0,M):
            b[s[i]-1]=c[i]
        print(b[0])
    else:
        b=[1]
        for i in range(0,N-1):
            b.append(0)
        for i in range(0,M):
            if s[i]==1 and c[i]==0:
                print("-1")
                break
        else:
            for i in range(0,M):
                b[s[i]-1]=c[i]
            for i in range(0,N):
                print(b[i],end='')
