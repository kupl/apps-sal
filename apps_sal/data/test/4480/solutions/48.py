class Solution:

    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        if sum(A) % 3:
            return False
        sumParts = sum(A) // 3
        summ = 0
        parts = 0
        for num in A:
            summ += num
            if summ == sumParts:
                parts += 1
                summ = 0
        return parts >= 3
