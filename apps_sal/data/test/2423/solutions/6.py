n=int(input())
arr=[]
for _ in range(n):
    arr.append(0)
for _ in range(n-1):
    a,b=list(map(int,input().split()))
    arr[a-1]+=1 
    arr[b-1]+=1 
print(arr.count(1))

