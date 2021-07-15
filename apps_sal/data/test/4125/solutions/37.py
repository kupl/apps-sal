import math

def gcd_list(nums):
  gcd = nums[0]
  for i in range(1,len(nums)):
    gcd = math.gcd(gcd,nums[i])
  return gcd

N,X = map(int,input().split())
x = list(map(int,input().split()))

x = [abs(i-X) for i in x]

print(gcd_list(x))
