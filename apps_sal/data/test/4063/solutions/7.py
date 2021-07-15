N  = int(input())
nums = list(map(int,input().split()))
nums.sort()
cnt = nums[N//2] - nums[N//2-1] 
print(cnt)
