n=int(input())
arr=list(map(int,input().strip().split(' ')))
arr=set(arr)
if 0 in arr:
  print(len(arr)-1)
else:
  print(len(arr))
