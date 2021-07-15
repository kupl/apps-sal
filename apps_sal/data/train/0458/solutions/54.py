class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        prefixSum = [0]
        for i in range(n):
            prefixSum.append(prefixSum[-1] + nums[i])
            
        minSubl = float('inf')
        modLastIdx = {}
        for i in range(1, n):
            modLastIdx[prefixSum[i] % p] = i
            r = prefixSum[n] - prefixSum[i]
            r_mod = r%p
            l_mod = (p - r%p) if r_mod > 0 else 0
            if l_mod in modLastIdx:
                preIdx = modLastIdx[l_mod]
                rmSubl = i - preIdx
                minSubl = min(minSubl, rmSubl)
        
        # last one
        l_mod = prefixSum[n] % p
        if l_mod == 0:
            minSubl = 0
            
        if l_mod in modLastIdx:
            preIdx = modLastIdx[l_mod]
            rmSubl = preIdx
            minSubl = min(minSubl, rmSubl)
            
        if 0 in modLastIdx:
            preIdx = modLastIdx[0]
            rmSubl = n - preIdx
            minSubl = min(minSubl, rmSubl)
            
        return minSubl if minSubl < float('inf') else -1
