N = int(input())
T = []

for i in range(N):
  T.append(int(input()))

import math

def lcm(m,n):
  return (m*n)//math.gcd(m,n)

def lcm_list(nums):
  lcm_num = nums[0]
  for i in range(1,len(nums)):
    lcm_num = lcm(lcm_num,nums[i])
  return lcm_num

print(lcm_list(T))
