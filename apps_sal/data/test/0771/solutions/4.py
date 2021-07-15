n,k,m=map(int,input().split())
a=list(map(int,input().split()))
b=[]
for i in range(m):
    b.append([])
for i in range(len(a)):
    b[a[i]%m].append(a[i])
for i in range(len(b)):
    if len(b[i])>=k:
        j=0
        print('Yes')
        while j<k:
            print(b[i][j],end=' ')
            j+=1
        break
else:
    print('No')
