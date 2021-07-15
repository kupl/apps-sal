class Solution:
    def maxScore(self, l: List[int], k: int) -> int:
        length = len(l)
        
        if k == length:
            return sum(l)
        elif k == 0:
            return 0
        
        k = length - k
        v = curr_min = sum(l[:k])
        
        for i in range(k,length):
            v =  v - l[i-k] + l[i]
            curr_min = min(curr_min, v)
        
        return sum(l) - curr_min

