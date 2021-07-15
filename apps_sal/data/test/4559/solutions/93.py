N = int(input())
nums = [int(i) for i in input().split()]


def calc(N, nums):
    ans = 1
    flg = False
    if 0 in nums:
        return 0
    for i in range(N):
        ans *= nums[i]
        if ans > 10 ** 18:
            flg = True
            break
    if flg:
        return -1
    else:
        return ans


print(calc(N, nums))
