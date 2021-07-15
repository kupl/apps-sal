class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        n = len(s)
        res_dict = collections.defaultdict(int)
        
        for lidx in range(n-minSize+1):
            lval = lidx+minSize
            rval = min(n,lidx+maxSize+1)
            for ridx in range(lval, 1+rval):
                counts = collections.Counter(s[lidx:ridx])
                if len(counts) <= maxLetters:
                    res_dict[s[lidx:ridx]] += 1
                else: 
                    break
        
        return max(res_dict.values()) if res_dict else 0
