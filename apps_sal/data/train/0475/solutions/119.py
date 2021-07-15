class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        result = []
        i = 0
        while(i < len(nums)):
            total = nums[i]
            result.append(total)
            j = i+1
            while(j < len(nums)):
                total += nums[j]
                result.append(total)
                j+=1
            i += 1
        result = sorted(result)
        return sum(result[left-1:right]) % ((10**9)+7)
