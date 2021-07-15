r,c=list(map(int,input().split()))

L=[]

for i in range(r):
    s=input()
    L.append(str(s))
ans=r*c
for i in range(r):
    for j in range(c):
        if(L[i][j]=="S"):
            ans-=1
            continue
        if("S" in L[i]):
            case=False
            for z in range(r):
                if(L[z][j]=="S"):
                    case=True
                    break
            if(case):
                ans-=1
print(ans)

