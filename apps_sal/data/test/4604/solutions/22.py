N = int(input())
As = list(map(int, input().split()))
# 絶対値の差は、
# 奇数の場合はN+1から2ずつ減らして行った分しかない。(N+1)/2
# 偶数の場合はNから2ずつ減らして行った分しかない。N/2
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
            # 絶対値の差は0の時は1人だけ。そのほかは2人だけ。これが満たせるなら
            # (偶数)2**(N+1/2)
            # (奇数)2**(N/2)
    print(ans)

