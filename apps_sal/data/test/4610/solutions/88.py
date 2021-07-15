n,k=list(map(int,input().split()))
a=[int(i) for i in input().split()]
c=[0]*(n+1)
for i in a:
    c[i]+=1
print((sum(sorted(c)[:-k])))

