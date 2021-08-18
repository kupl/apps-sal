n, a, b = list(map(int, input().split()))
arr = list(map(int, input().split()))

sum = 0
for i in range(n // 2):
    nums = sorted((arr[i], arr[-1 - i]))
    if nums[0] == 0 and nums[1] == 1:
        print(-1)
        return
    elif nums[0] == 2 and nums[1] == 2:
        sum += 2 * min(a, b)
    elif nums[0] == 0 and nums[1] == 2:
        sum += a
    elif nums[0] == 1 and nums[1] == 2:
        sum += b

if n % 2 == 1:
    if arr[n // 2] == 2:
        sum += min(a, b)

print(sum)
