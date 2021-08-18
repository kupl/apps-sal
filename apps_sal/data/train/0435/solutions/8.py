class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        res = 0
        currsum = 0
        d = Counter()
        d[0] = 1
        for i, num in enumerate(A):
            currsum += num
            currsum %= K
            if currsum in d:
                res += d[currsum]
            d[currsum] += 1
        return res
