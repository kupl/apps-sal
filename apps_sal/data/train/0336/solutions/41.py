class Solution:
    def minSteps(self, s: str, t: str) -> int:
        countS = Counter(s)
        countT = Counter(t)
        index = 0
        res = 0
        if countS == countT:
            return 0
        
        # for k, v in countT.items():
        #     if v < countS[k]:
        #         res += countS[k] - v
        
        for k, v in countS.items():
            if v > countT[k]:
                res += v - countT[k]
            
        return res
