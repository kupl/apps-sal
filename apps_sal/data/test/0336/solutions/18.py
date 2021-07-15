import sys

arr = list(map(int, input().strip().split()))
n = arr[0]
top = arr[1]
left = arr[2]
right = arr[3]
bottom = arr[4]

top_left = top + left
top_right = top + right
bottom_left = bottom + left
bottom_right = bottom + right

max_greater = 0
max_lesser = 0
nums = [top_right, bottom_left, bottom_right]
for e in nums:
    diff = e - top_left
    max_greater = max(max_greater, diff)
    max_lesser = min(max_lesser, diff)
max_diff = max_greater - max_lesser

if max_diff > n - 1:
    ans = 0
else:
    ans = (n - max_diff) * n
print(ans)

