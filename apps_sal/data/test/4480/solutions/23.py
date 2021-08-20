class Solution:

    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total = sum(A)
        third = total // 3
        (cumsum, count) = (0, 0)
        for i in range(0, len(A)):
            cumsum += A[i]
            if cumsum == third:
                count += 1
                cumsum = 0
        return count == 3 or (count > 3 and total == 0)
