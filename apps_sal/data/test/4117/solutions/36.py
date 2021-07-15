N = int(input())
nums = [int(i) for i in input().split()]
nums =sorted(nums)
ans = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            # 1つ目の条件
            if nums[i] != nums[j] and nums[j] != nums[k]:
                # 2つ目の条件
                if nums[i] + nums[j] > nums[k]:
                    ans += 1
                    
print(ans)
