n,k=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
al=sum(l)
for i in range(n-k):
    al -= l[i]
print(al)
