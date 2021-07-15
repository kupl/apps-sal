for _ in range(int(input())):
    n,k=list(map(int,input().split()))
    arr=list(map(int,input().split()))
    if k==1 and sum(arr)%2:
        print("YES")
        print(n)
        continue
    elif k==1:
        print("NO")
        continue
    ans=[]
    tot=0
    for ind,i in enumerate(arr):
        tot+=i
        if tot%2:
            k-=1
            ans.append(ind+1)
            tot=0
            if not k:
                break
    if tot!=0 and tot%2==0 or k!=0:
        print("NO")
        continue
    temp=sum(arr[ans[-2]:])
    if temp%2:
        print("YES")
        ans.pop()
        for j in ans:
            print(j,end=" ")
        print(n)
    else:
        print("NO")
