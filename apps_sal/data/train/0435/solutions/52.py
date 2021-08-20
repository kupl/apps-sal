class Solution:

    def subarraysDivByK(self, A: List[int], K: int) -> int:
        preSum = [0]
        for num in A:
            preSum.append((preSum[-1] + num) % K)
        preSumCounter = Counter(preSum)
        return sum((v * (v - 1) // 2 for v in preSumCounter.values()))
