class Solution:
    def addOrIncrement(self, key, dictionary):
        if key in dictionary:
            dictionary[key] += 1
        else:
            dictionary[key] = 1
    
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n < k:
            return 0
        
        ans = 0
        seen = {0: 1}
        curVal = 0
        for num in nums:
            curVal += 0 if num % 2 == 0 else 1
            if curVal - k in seen:
                ans += seen[curVal - k]
            self.addOrIncrement(curVal, seen)
        
        return ans

