
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        num_odd = 0
        start = 0
        output = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                num_odd += 1
            while num_odd > k:
                if nums[start] % 2 == 1:
                    num_odd -= 1
                start += 1
            if num_odd == k:
                output += 1
                cur_start = start
                while nums[cur_start] % 2 == 0:
                    cur_start += 1
                    output += 1
        return output
