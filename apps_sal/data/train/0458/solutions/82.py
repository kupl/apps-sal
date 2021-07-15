from collections import defaultdict, Counter
from bisect import bisect
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        sum_nums = sum(nums)
        n = len(nums)
        if sum_nums % p == 0:
            return 0
        desired_rem = sum_nums % p
        mapping = defaultdict(list)
        pref_arr = [0]
        for i, num in enumerate(nums):
            if num % p == desired_rem:
                return 1
            temp = (pref_arr[-1] + num) % p
            mapping[temp].append(i)
            pref_arr.append(temp)
        
        
        ans = float('inf')
        # need to find shortest subarray who's sum % p == sum_nums % p

        # loop through all indices and see if sub-array possible starting at that index
        for i in range (n + 1):
            r = (desired_rem + pref_arr[i])%p
            if r not in mapping:
                continue 
            arr = mapping[r]
            index = bisect(arr, i)
            if index == len(arr):
                continue
            ans = min(ans, arr[index] - i + 1)
        
        return ans if ans < n else -1
        
        

