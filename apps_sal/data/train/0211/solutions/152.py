class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        res = 1
        upper = 2 ** (len(s) - 1) # so many possible breaks
        
        for i in range(upper):
            words = []
            prev = 0
            for pos in range(len(s) - 1):
                t = pos + 1
                if 1 << pos & i:
                    words.append(s[prev:t])
                    prev = t
            words.append(s[prev:])
            if len(words) == len(set(words)):
                #print(words)
                res = max(res, len(words))
        return res
            

