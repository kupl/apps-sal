from bisect import bisect_right


def getN():
    return int(input())


def getList():
    return list(map(int, input().split()))


n = getN()
nums = [abs(i) for i in getList()]
nums.sort(reverse=False)
ans = 0
for i, num in enumerate(nums):
    ans += bisect_right(nums, num * 2) - i - 1

print(ans)
