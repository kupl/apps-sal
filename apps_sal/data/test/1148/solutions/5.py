n = int(input())
nums = list(map(int, input().split()))
m = min(nums)
x = [num > m for num in nums]
x = x + x
left = 0
right = 0
ans = 0
while right < 2 * n:
    if left == right:
        right += 1
    elif not x[left]:
        left += 1
    elif x[right]:
        right += 1
    else:
        ans = max(ans, right - left)
        left = right
print(n * m + ans)
