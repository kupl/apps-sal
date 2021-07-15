N=int(input())
Hlist=list(map(int,input().split()))
minh=Hlist[0]
for i in range(N-1):
    if minh>Hlist[i+1]:
        print('No')
        return
    elif Hlist[i+1]>minh:
        minh=Hlist[i+1]-1
print('Yes')
