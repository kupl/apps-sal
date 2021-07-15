N = int(input())
nums = [int(i) for i in input().split()]

before = 0
ans = 0
for i in range(N):
    if i == 0:
        before =nums[i]
        continue
    if before > nums[i]:
        ans +=before - nums[i]
    else:
        before = nums[i]

print(ans)

