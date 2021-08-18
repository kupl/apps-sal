N = int(input())
As = list(map(int, input().split()))
nums = {}
exists = True
if N % 2 == 0:
    for A in As:
        if A in nums:
            nums[A] += 1
        else:
            nums[A] = 1
    for key, value in list(nums.items()):
        if key == 0:
            exists = False
        if value != 2:
            exists = False

else:
    for A in As:
        if A in nums:
            nums[A] += 1
        else:
            nums[A] = 1
    for key, value in list(nums.items()):
        if key == 0:
            if value != 1:
                exists = False
        else:
            if value != 2:
                exists = False
if not exists:
    print((0))
else:
    ans = 1
    if N % 2 == 0:
        for i in range(int(N / 2)):
            ans = ans * 2
            ans %= 10**9 + 7
    else:
        for i in range(int((N - 1) / 2)):
            ans = ans * 2
            ans %= 10**9 + 7
    print(ans)
