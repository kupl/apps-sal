q = int(input())
n = 10 ** 5 + 1
flag = [True] * n
flag[1] = False
for i in range(4, n, 2):
    flag[i] = False
for i in range(3, int(n ** 0.5) + 1, 2):
    if flag[i]:
        for j in range(i + i, n, i):
            flag[j] = False
nums = [0] * n
for i in range(1, n):
    if i % 2 == 1:
        if flag[i] and flag[(i + 1) // 2]:
            nums[i] = nums[i - 1] + 1
        else:
            nums[i] = nums[i - 1]
    else:
        nums[i] = nums[i - 1]
for _ in range(q):
    (l, r) = map(int, input().split())
    print(nums[r] - nums[l - 1])
