n,m=list(map(int,input().split()))
c=[]
cnt=0
for i in range(n):
    a=list(map(int,input().split()))
    for j in range(1,len(a)):
        c.append(a[j])
    
for j in range(1,m+1):
    if c.count(j)==n:
        cnt += 1
print(cnt)

