class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        result = 0
        start, count = 0, 0
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                count += 1
            while start < i and count > k:
                if nums[start] % 2 != 0:
                    count -= 1
                start += 1
            if count == k:
                result += 1
            for j in range(start, i):
                if count == k and nums[j] % 2 == 0:
                    result += 1
                else:
                    break
        return result
