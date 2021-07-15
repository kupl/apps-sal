class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        j = i = count = ret = 0
        for n in nums:
            if n%2: count += 1
            if count == k:
                i = j
                while count == k:
                    count -= 1 if nums[j] % 2 else 0
                    j += 1
            ret += j - i
        return ret
            

