import numpy as np
(N, K) = list(map(int, input().split()))
S = list(input())
nums = []
now = 1
cnt = 0
for s in S:
    if s == str(now):
        cnt += 1
    else:
        nums.append(cnt)
        now = 1 - now
        cnt = 1
if cnt != 0:
    nums.append(cnt)
if len(nums) % 2 == 0:
    nums.append(0)
sums = [0] + list(np.cumsum(nums))
left = 0
right = left + K * 2
maxi = 0
if N < 3:
    maxi = N
while right < len(nums):
    if sums[right + 1] - sums[left] > maxi:
        maxi = sums[right + 1] - sums[left]
    right += 2
    left += 2
if maxi == 0:
    maxi = sum(nums)
print(maxi)
