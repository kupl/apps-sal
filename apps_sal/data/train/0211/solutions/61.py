class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        
        
        # my solution after contest ends ... 68 ms ... 80 % ... 13.6 MB ... 100 %
        #  time: O()
        # space: O()
        
        def backtrack(seen, sidx):
            if sidx == len(s):
                self.res = max(self.res, len(seen))
                return
            if len(seen) + len(s) - sidx <= self.res:  # 截断条件提速  600 ms ===> 68 ms
                return
            for eidx in range(sidx, len(s)):
                if s[sidx:eidx+1] not in seen:
                    backtrack(seen | {s[sidx:eidx+1]}, eidx+1)
        self.res = 1
        backtrack(set(), 0)
        return self.res
        
        

