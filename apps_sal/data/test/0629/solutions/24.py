N=int(input())
x=[[0]*N,[0]*N]
a=list(map(int,input().split()))
adash=[0]
for i in range(N-1):
    adash.append(adash[-1]+a[i])
b=list(map(int,input().split()))
bdash=[0]
for i in range(N-1):
    bdash.append(bdash[-1]+b[i])
c=list(map(int,input().split()))
kachra=[]
for i in range(N):
    kachra.append(adash[i]+c[i]+bdash[-1]-bdash[i])
kachra.sort()
print(kachra[0]+kachra[1])

