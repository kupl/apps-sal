n,m,d=map(int,input().split())
a=list(map(int,input().split()))
o=[0]*n
x=[(a[i],i) for i in range(n)]
x.sort()
u=0
i=j=0
while i<n:
    if x[i][0]-d<=x[j][0]:u+=1;o[x[i][1]]=u
    else:o[x[i][1]]=o[x[j][1]];j+=1
    i+=1
print(u)
print(' '.join(list(map(str,o))))
