"""
keyword: 尺取法
"""
import sys
sys.setrecursionlimit(10 ** 6)
(n, k) = map(int, input().split())
s = input()
nums = []
now = 1
cnt = 0
for i in range(n):
    if s[i] == str(now):
        cnt += 1
    else:
        nums.append(cnt)
        now ^= 1
        cnt = 1
if cnt != 0:
    nums.append(cnt)
if len(nums) % 2 == 0:
    nums.append(0)
add = 2 * k + 1
ans = 0
left = 0
right = 0
tmp = 0
for i in range(0, len(nums), 2):
    nextleft = i
    nextright = min(i + add, len(nums))
    while nextleft > left:
        tmp -= nums[left]
        left += 1
    while nextright > right:
        tmp += nums[right]
        right += 1
    ans = max(tmp, ans)
print(ans)
