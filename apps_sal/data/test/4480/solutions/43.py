class Solution:
    def canThreePartsEqualSum(self, li: List[int]) -> bool:
        s = sum(li)
        if s % 3: return False
        ts = s // 3
        ss = 0
        chunk = 0
        for n in li[:-1]:
            ss += n
            if ss == ts:
                chunk += 1
                if chunk == 2:
                    return True
                ss = 0
        return False
