N, M=map(int, input().split())
nums=[0]*(N+1)
for _ in range(M):
  a, b=map(int, input().split())
  nums[a]+=1
  nums[b]+=1
print(*nums[1:], sep='\n')
