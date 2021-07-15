n=int(input())
a=list(map(int,input().split()))
s=0
k=0
for i in range(n):
    if a[i]>=4:
        k+=1
    else:
        k=0
    if k==3:
        k=0
        s+=1
print(s)

