"""
[4,5,0,-2,-3,1]

"""


class Solution:

    def subarraysDivByK(self, A: List[int], K: int) -> int:
        d = {0: 1}
        runningSum = 0
        sol = 0
        for i in range(len(A)):
            runningSum += A[i]
            newMod = runningSum % K
            if newMod not in d:
                d[newMod] = 0
            d[newMod] += 1
            sol += d[newMod] - 1
        return sol
