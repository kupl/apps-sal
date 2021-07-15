class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        N = len(nums)
        freqCount = [0 for i in range(N+1)]
        umap = dict()
        minFreq = 1
        maxFreq = 1
        umap[nums[0]] = 1
        freqCount[1] = 1
        result = 1
        
        for i in range(1, N):
            if nums[i] not in umap:
                umap[nums[i]] = 1
                minFreq = 1
            else:
                freqCount[umap[nums[i]]] -= 1
                if freqCount[umap[nums[i]]] == 0 and minFreq == umap[nums[i]]:
                    minFreq = umap[nums[i]] + 1
                umap[nums[i]] += 1
            freqCount[umap[nums[i]]] += 1
            
            if umap[nums[i]] > maxFreq:
                maxFreq = umap[nums[i]]
            
            if maxFreq == minFreq+1 and freqCount[maxFreq] == 1:
                result = i+1
            if maxFreq == minFreq and freqCount[maxFreq] == i+1:
                result = i + 1
            if maxFreq == minFreq and freqCount[maxFreq] == 1:
                result = i + 1
            if maxFreq * freqCount[maxFreq] == i:
                result = i + 1
                
        return result

