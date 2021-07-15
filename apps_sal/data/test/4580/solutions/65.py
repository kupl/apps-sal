n=int(input())
a=list(map(int,input().split()))
b=[]
c=[0]*8
d=0
for i in a:
    if i<3200:
        b.append(i)
    else:
        d+=1
for i in range(len(b)):
    for j in range(8):
        if 400*j<=b[i]<400*(j+1):
            c[j]=1
print(max(sum(c),1),sum(c)+d)
