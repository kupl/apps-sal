Q = int(input())
for q in range(Q):
    (n, k, d) = tuple(map(int, input().split()))
    arr = list(map(int, input().split()))
    nums = {}
    for i in range(d):
        if arr[i] in nums:
            nums[arr[i]] += 1
        else:
            nums[arr[i]] = 1
    ans = len(nums)
    for i in range(d, n):
        if nums[arr[i - d]] == 1:
            nums.pop(arr[i - d])
        else:
            nums[arr[i - d]] -= 1
        if arr[i] in nums:
            nums[arr[i]] += 1
        else:
            nums[arr[i]] = 1
        ans = min(ans, len(nums))
    print(ans)
