n=int(input())
arr=[]
for _ in range(n):
    a,b=list(map(int,input().split()))
    arr.append([a,b])
ans=False
for i in range(1,n-1):
    if arr[i][0]==arr[i][1] and arr[i-1][0]==arr[i-1][1] and arr[i+1][0]==arr[i+1][1]:
        ans=True
        break
if ans :
    print("Yes")
else:
    print("No")

