class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        minlen = n = len(nums) #subarr length
        target = sum(nums) % p #sum of subarray that needs to be removed
        if target == 0:
            return 0
        
        cursum = 0 #prefix sum
        dct = {0 : -1} # remainder : index
        
        for i, num in enumerate(nums):
            cursum = (cursum + num) % p
            dct[cursum] = i
            if (cursum - target) % p in dct:
                minlen = min(minlen, i - dct[(cursum - target) % p])
                
        return -1 if minlen>=n else minlen
        

