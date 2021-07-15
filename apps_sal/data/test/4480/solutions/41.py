class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        s = sum(A)
        if s % 3 != 0:
            return False
        target = s//3
        current = 0
        count = 0
        for v in A:
            current += v
            if current == target:
                count += 1
                current = 0
                if count >= 3:
                    return True
        return False
