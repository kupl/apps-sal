a=list(map(int,input().split()))
count=0
for v in range(2):
    if a[0]>=a[1]:
        count+=a[0]
        a[0]-=1
    else:
        count+=a[1]
        a[1]-=1
print(count)
