n,k=input().split()
k=int(k)
l=list(map(int,input().split()))
l.sort()
sum=0
for i in range(0,k):
    sum+=l[i]
print(sum)
