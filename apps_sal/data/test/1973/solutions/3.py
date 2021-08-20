NUMS = [0 for i in range(10)]


def check(nums):
    maxi = max(nums)
    category = nums.count(maxi)
    if category == 1:
        oneof = 0
        for n in nums:
            if n == maxi:
                continue
            if n == 0:
                continue
            if oneof != 0 and (n != oneof or n != maxi - 1):
                return False
            oneof = n
        return True
    elif maxi != 1:
        if nums.count(1) != 1:
            return False
        if nums.count(0) != len(nums) - category - 1:
            return False
        return True
    else:
        return True


n = int(input())
colors = list(map(int, input().split()))
res = 0
for i in range(n):
    NUMS[colors[i] - 1] += 1
    if check(NUMS):
        res = i + 1
print(res)
