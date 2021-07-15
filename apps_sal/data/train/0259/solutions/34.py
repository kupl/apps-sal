class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        nums.sort()
        n = len(nums)
        
        start, end = 1, nums[-1]
        while start < end:
            mid = (start + end) // 2
            j = n - 1
            s = n
            while j >= 0 and mid < nums[j]:
                s -= 1
                s += math.ceil(nums[j] / mid)
                j -= 1
            if s > threshold:
                start = mid + 1
            else:
                end = mid
        return start
        # j = len(nums) - 1
        # for i in nums[::-1]:
        #     j = n - 1
        #     s = n
        #     while j >= 0 and i < nums[j]:
        #         s -= 1
        #         s += math.ceil(nums[j] / i)
        #         j -= 1
        #     if s > threshold:
        #         start = i
        #         end = prev
        #         break
        #     prev = i
        # else:
        #     start = 1
        #     end = i
        # # print(start, end)   
        # for i in range(end, start - 1, -1):
        #     j = n - 1
        #     s = n
        #     while j >= 0 and i < nums[j]:
        #         s -= 1
        #         s += math.ceil(nums[j] / i)
        #         j -= 1
        #     if s > threshold:
        #         return i + 1
        # return 1

