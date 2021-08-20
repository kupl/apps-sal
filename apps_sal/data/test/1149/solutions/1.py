n = int(input())
b = [0 for i in range(n)]
nums = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
for i in range(1, len(nums)):
    b[nums[i] - 1] = 1
for i in range(1, len(nums2)):
    b[nums2[i] - 1] = 1
if sum(b) == n:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')
