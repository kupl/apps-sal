class Solution:

    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        s = sum(A)
        if s % 3 != 0:
            return False
        target = s / 3
        total = 0
        partitions = 0
        for num in A:
            total += num
            if total == target:
                partitions += 1
                total = 0
        return total == 0 and partitions in [3, 4]
