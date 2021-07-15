n=int(input())
arr=list(map(int,input().split()))
arr.sort()
val1=max(arr)-min(arr[1:])
val2=max(arr[:n-1])-min(arr)
print(min(val1,val2))

