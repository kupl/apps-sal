n=int(input())
nums=list(map(int,input().split()))
setnum=set(nums)
if(len(setnum)==n):
  print("YES")
else:
  print("NO")
