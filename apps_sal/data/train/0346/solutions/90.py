class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        flattened = [1 if num % 2 == 1 else 0 for num in nums]
        
        d = { 0: 1 }
        sum = 0
        total = 0
        
        for i in range(len(flattened)):
            sum += flattened[i]
            total += d.get(sum - k, 0)
            d[sum] = d.get(sum, 0) + 1
        
        return(total)

