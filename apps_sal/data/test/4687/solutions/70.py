N,K = map(int,input().split())
nums = []

for _ in range(N):
  a,b = map(int,input().split())
  nums.append([a,b])

nums.sort()
S = 0

for i in range(N+1):
  if S < K:
    S += nums[i][1]
  else:
    print(nums[i-1][0])
    break
