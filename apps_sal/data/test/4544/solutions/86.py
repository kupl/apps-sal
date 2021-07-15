N = int(input())
A = list(map(int,input().split()))
nums = [0]*100000
ans_list=[]

for i in range(N):
  nums[A[i]] += 1

for j in range(1,99999):
  ans_list.append(nums[j-1]+nums[j]+nums[j+1])

print(max(ans_list))
