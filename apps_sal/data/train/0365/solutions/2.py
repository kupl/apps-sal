class Solution:
    def uniqueLetterString(self, s: str) -> int:
        if not s:
            return 0
        
        ind = defaultdict(list)
        for i, ch in enumerate(s):
            ind[ch].append(i)
        
        res = 0
        for seq in ind.values():
            for i, index in enumerate(seq):
                len_left, len_right = 0, 0
                if i > 0:
                    len_left = index - seq[i - 1] - 1
                else:
                    len_left = index
                
                if i + 1 < len(seq):
                    len_right = seq[i + 1] - index - 1
                else:
                    len_right = len(s) - index - 1
                
                res += ((len_left + 1) * (len_right + 1))
        
        return res
