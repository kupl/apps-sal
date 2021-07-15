n,k=map(int,input().split(' '))
l=[]
l1=[]
for i in range(0,n):
    s=input()
    l.append(s)
    l1.append(n*[0])
a1=1
a2=1
maxx=0
for i in range(0,n):
    for j in range(0,n-k+1):
        if (l[i])[j:j+k]==k*".":
            for m in range(0,k):
                l1[i][j+m]+=1
                if l1[i][j+m]>maxx:
                    maxx=l1[i][j+m]
                    a1=i+1
                    a2=j+m+1
l2=[]
for i in range(0,n):
    s=""
    for j in range(0,n):
        s+=l[j][i]
    l2.append(s)
for i in range(0,n):
    for j in range(0,n-k+1):
        if (l2[i])[j:j+k]==k*".":
            for m in range(0,k):
                l1[j+m][i]+=1
                if l1[j+m][i]>maxx:
                    maxx=l1[j+m][i]
                    a1=j+m+1
                    a2=i+1
print(a1,a2)
