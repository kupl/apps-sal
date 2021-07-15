def getN():
    return int(input())
def getList():
    return list(map(int, input().split()))

from bisect import bisect_right

n = getN()
nums = [abs(i) for i in getList()]
nums.sort(reverse=False)
ans = 0
#print(nums)
for i , num in enumerate(nums):
    ans += bisect_right(nums, num*2) - i - 1

print(ans )

