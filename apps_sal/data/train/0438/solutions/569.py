class Solution:
    def findLatestStep(self, a: List[int], m: int) -> int:
        if m == len(a): return len(a)
        index2len, ans = defaultdict(int), -1        
        for i, p in enumerate(a):    
            l, r = index2len[p-1], index2len[p+1]      
            if l == m or r == m: ans = i
            index2len[p-l] = index2len[p+r] = l + 1 + r            
        return ans
