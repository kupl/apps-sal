import sys
lines = sys.stdin.readlines()
T = int(lines[0].strip())
for t in range(T):
    n = int(lines[2 * t + 1].strip())
    nums = list(map(int, lines[2 * t + 2].strip().split(" ")))
    res = []
    tmp = nums[0]
    for i in range(1, len(nums)):
        if nums[i] * nums[i - 1] > 0:
            tmp = max(tmp, nums[i])
        else:
            res.append(tmp)
            tmp = nums[i]
    res.append(tmp)
    print(sum(res))
