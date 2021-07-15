class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        # get the most freq occurring ints 
        d = {}
        for a in arr:
            if a in d:
                d[a] += 1
            else:
                d[a] = 1
        
        q = []
        for k in d:
            heappush(q, (-d[k], k))
        
        size = len(arr)
        half = len(arr) / 2
        numPop = 0
        while size > half:
            poped = heappop(q)
            size += poped[0]
            numPop += 1
        
        return numPop
