(n, k) = map(int, input().split())
s = input()
nums = []
if s[0] == '0':
    nums.append(0)
i = 0
while i < n:
    j = i
    while j < n and s[j] == s[i]:
        j += 1
    nums.append(j - i)
    i = j
if s[-1] == '0':
    nums.append(0)
sums = [0]
for i in range(len(nums)):
    sums.append(sums[-1] + nums[i])
res = 0
for left in range(0, len(sums), 2):
    right = left + k * 2 + 1
    if right >= len(sums):
        right = len(sums) - 1
    res = max(res, sums[right] - sums[left])
print(res)
