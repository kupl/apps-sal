n=int(input())
arr=[int(i) for i in input().split()]
ans=0
for i in arr:
    ans+=i
if ans%2!=0:
    print("NO")
else:
    if n==1:
        if arr[0]%2==0:
            print("YES")
        else:
            print("NO")
    else:
        flag=0
        for i in range(0,n-1):
            if arr[i]<0:
                flag=1
                break
            arr[i]%=2
            if arr[i]==1:
                arr[i]=0
                arr[i+1]-=1
        if flag==1:
            print("NO")
        else:
            if arr[n-1]<0 or arr[n-1]%2!=0:
                print("NO")
            else:
                print("YES")

