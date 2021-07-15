n,m=map(int,input().split())
q=[list(map(int,input().split())) for _ in range(m)]
for i in range(10**n):
    i=str(i)
    if len(i)!=n:
        continue
    f=1
    for j in q:
        if i[j[0]-1]!=str(j[1]):
            f=0
            break
    if f:
        print(i)
        return
print("-1")
