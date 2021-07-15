L,R = map(int,input().split())
ans = 0

if R-L < 2018:
  nums = list(range(L,R+1))
  A = []
  for i in range(len(nums)):
    for j in range(i+1,len(nums)):
      A.append((nums[i]*nums[j])%2019)
  ans = min(A)

print(ans)
