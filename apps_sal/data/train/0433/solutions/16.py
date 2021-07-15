class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        presum = [0]
        
        for num in arr:
            presum.append( presum[-1]+num )
        
        res = 0
        i=0
        while i+k < len(presum):
            if presum[i+k]-presum[i] >= threshold*k:
                res += 1
            i+= 1
        
        return res
