class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        s = sum(A)
        if s % 3 != 0:
            return False
        ps = s // 3
        count = 0
        for x in A:
            ps -= x
            if not ps:
                ps = s // 3
                count += 1
        return count >= 3
