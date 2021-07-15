n,m=map(int,input().split())
blist=[int(x) for x in input().split()]
llist=[0]*n

for i in range(m):
    for j in range(blist[i]-1,n):
        if llist[j]==0:
            llist[j]=blist[i]

print(''.join([str(llist[i])+' ' for i in range(n)]))
