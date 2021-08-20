class Solution:

    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        tot = sum(A)
        if tot % 3 != 0:
            return False
        flag = 0
        temp_tot = 0
        presum = [0] * (len(A) + 1)
        s = tot // 3
        target = [2 * s, s]
        for i in range(len(A)):
            if not target:
                return True
            presum[i + 1] = presum[i] + A[i]
            if presum[i + 1] == target[-1]:
                target.pop()
        return False
