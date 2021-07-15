n,m=list(map(int,input().split()))
ls=[[] for i in range(m) ]
for i in range(n):
    a,b,c=input().split()
    b,c=int(b),int(c)
    ls[b-1].append([a,c])

for i in range(m):
    ls[i].sort(key=lambda x: x[1],reverse=True)
    #print(ls[i])
    if len(ls[i])>2 and ls[i][1][1]==ls[i][2][1]:
        print("?")
    else :
        print(ls[i][0][0],ls[i][1][0])

