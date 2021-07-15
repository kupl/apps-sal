class Solution:
    def maxLength(self, arr: List[str]) -> int:
        if len(arr) == 0:
            return 0
        currRes = []
        for el in arr:
            if self.isUnique(el):
                currRes.append(el)
                
        for el in arr:
            for subSeq in currRes:
                if self.isUnique(el + subSeq):
                    currRes.append(el+subSeq)
        res = 0
        for el in currRes:
            res = max(res, len(el))
        return res
    
    def isUnique(self, s):
        return len(set(s)) == len(s)
