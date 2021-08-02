t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    currentmax = nums[0]
    ans = 0
    if nums[0] > 0:
        pos = 1
    else:
        pos = -1
    for j in range(1, n):
        if nums[j] > 0:
            if pos == 1:
                if nums[j] > currentmax:
                    currentmax = nums[j]
            else:
                ans = ans + currentmax
                currentmax = nums[j]
                pos = 1
        else:
            if pos == -1:
                if nums[j] > currentmax:
                    currentmax = nums[j]
            else:
                ans = ans + currentmax
                currentmax = nums[j]
                pos = -1
    ans = ans + currentmax
    print(ans)
