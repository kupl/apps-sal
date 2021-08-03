TC = int(input())

for _ in range(TC):
    a, b, c = list(map(int, input().split()))

    nums = sorted((a, b, c))

    cnt = 0
    for i in range(2, -1, -1):
        if nums[i] > 0:
            nums[i] -= 1
            cnt += 1

    if nums[2] > 0 and nums[1] > 0:
        cnt += 1
        nums[2] -= 1
        nums[1] -= 1

    if nums[2] > 0 and nums[0] > 0:
        cnt += 1
        nums[2] -= 1
        nums[0] -= 1

    if nums[1] > 0 and nums[0] > 0:
        cnt += 1
        nums[1] -= 1
        nums[0] -= 1

    if all(nums):
        cnt += 1

    print(cnt)
