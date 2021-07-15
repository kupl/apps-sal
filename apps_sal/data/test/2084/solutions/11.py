n,k=list(map(int, input().split()))
a=sorted([int(i) for i in input().split()])
s=0
for i in range(k):
    s+=a[i]
print(s)


