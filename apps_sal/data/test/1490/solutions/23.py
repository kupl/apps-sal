n,m=map(int,input().split(' '))
a=[int(i) for i in input().split(' ')]
a=set(a)
b=[]
cc=0
lim=int(1e9)
i=1
while i<=m:
    if i not in a:
        cc+=1
        b.append(i)
        m-=i
    i+=1
print(cc)
for i in range(len(b)):
    print(b[i],end=' ')


