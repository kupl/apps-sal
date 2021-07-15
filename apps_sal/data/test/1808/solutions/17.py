n,k,x=map(int,input().split())
nums=list(map(int,input().split()))
for i in range(k):
  nums[n-i-1]=x
print(sum(nums))
