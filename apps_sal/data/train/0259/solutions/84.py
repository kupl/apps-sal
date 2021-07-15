import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # max = 0
        # for j in range(threshold):
        #     count = 0
        #     for i in range(len(nums)):
        #         a = nums[i]/(j+1)
        #         count += math.ceil(a)
        #     print(count)
        #     if count <= threshold:
        #         if max < count:
        #             max = count
        # return j
        def checking(mid):
            ans = 0
            for num in nums:
                ans += math.ceil(num/mid)
                if ans > threshold:
                    return False
            return True
        l, r = 1, int(1e6)
        while l<= r:
            mid = (l+r)//2
            if checking(mid):
                r = mid-1
            else:
                l = mid+1
        return l

