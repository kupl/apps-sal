N=int(input())
p=list(map(int,input().split()))
count=0
f=0
for i in range(N):
    if f:
        f=0
        continue
    if p[i]==i+1:
        count+=1
        f=1
print(count)
