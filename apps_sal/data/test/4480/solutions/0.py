class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:

        if len(A) < 3:
            return False
        suma = sum(A)
        if suma % 3 != 0:
            return False

        runsum, target, count = 0, suma / 3, 0

        for val in A[:-1]:
            runsum += val
            if runsum == target:
                count += 1
                runsum = 0
                if count == 2:
                    return True
        else:
            return False
