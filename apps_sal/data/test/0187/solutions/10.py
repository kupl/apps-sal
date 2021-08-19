def solve():
    n = int(input())
    nums = [int(input()) for i in range(n)]
    numdict = {}
    for num in nums:
        if num in numdict:
            numdict[num] += 1
        else:
            numdict[num] = 1
    if len(numdict) != 2:
        print('NO')
    else:
        nums = list(numdict.keys())
        if numdict[nums[0]] == numdict[nums[1]]:
            print('YES')
            print(nums[0], nums[1])
        else:
            print('NO')
    return


solve()
