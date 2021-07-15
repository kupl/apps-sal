t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    left=-1
    right=-1
    for i in range(n):
        if a[i]==1:
            left=i
            break
    if left==-1:
        print(0)
        continue
    for i in range(n-1,-1,-1):
        if a[i]==1:
            right=i
            break
    count1=0
    for i in range(n):
        if a[i]==1:
            count1+=1
    print(right-left-count1+1)
