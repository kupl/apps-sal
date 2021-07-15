t=int(input())
lst=list(map(int,input().split()))
for _ in range(len(lst)):
    n=lst[_]
    l=[[0]*n,[0]*n,[0]*n,[0]*n]
    
    c=1
    
    for i in range(n):
        for j in range(4):
            if j==2:
                continue
            else:
                l[j][i] = c
                c+=1
        l[2][i] = l[3][i] + l[0][i]
        c = l[2][i]
        
    for i in range(4):
        for j in range(n):
            if(j!=3):
                print(l[i][j],end=' ')
            else:
                print(l[i][j],end=' ')
        print()
