N=int(input())
A=list(map(int,input().split()))
mod = 10**9+7

A=tuple(sorted(A))

if N % 2 == 1:
  nums=[0]
  for i in range(2,N+1,2):
    nums.append(i)
    nums.append(i)
else:
  nums=[]
  for i in range(1,N+1,2):
    nums.append(i)
    nums.append(i)
    
nums = tuple(nums)
if A != nums:
  print(0)
  return
  
print(2**(N//2) % mod)
