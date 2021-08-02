n = int(input())
nums = list(map(int, input().split()))

right = [0 for i in range(n)]
for i in range(n - 1, -1, -1):
    right[i] = nums[i]
    if i < n - 1:
        right[i] += right[i + 1]

left = [0 for i in range(n)]
for i in range(n):
    left[i] = nums[i]
    if i > 0:
        left[i] += left[i - 1]

res = 0
for i in range(-1, n):
    count = 0
    if i >= 0:
        count = i + 1 - left[i]
    if i + 1 < n:
        count += right[i + 1]
    res = max(res, count)

print(res)
