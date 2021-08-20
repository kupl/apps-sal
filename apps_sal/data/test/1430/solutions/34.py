"""
keyword: 累積和
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
tot = [0] * (len(nums) + 1)
for i in range(len(nums)):
    tot[i + 1] = tot[i] + nums[i]
ans = 0
for i in range(0, len(nums), 2):
    left = i
    right = min(i + add, len(nums))
    tmp = tot[right] - tot[left]
    ans = max(tmp, ans)
print(ans)
