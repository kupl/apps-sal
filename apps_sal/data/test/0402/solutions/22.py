n,k=list(map(int,input().split()))
t=240-k
count=0
for i in range(1,n+1):
    if t-5*i>=0:
        t=t-5*i
        count+=1
print(count)

