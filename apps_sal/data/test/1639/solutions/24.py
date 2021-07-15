n=int(input())
arr=list(map(int, input().split()))
ans=1
temp=1
for i in range(1,n):
    if arr[i]>=arr[i-1]:
        temp+=1
    else:
        if temp>ans:
            ans=temp
        temp=1
print(max(ans, temp))

