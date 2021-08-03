class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        sums = []
        ss = 0
        maxi = 0
        for s, e in sorted([(speed[i], efficiency[i]) for i in range(n)], key=lambda x: [-x[1], -x[0]]):
            heappush(sums, s)
            ss += s
            if len(sums) > k:
                rmv = heappop(sums)
                ss -= rmv
            maxi = max(maxi, ss * e)

        return maxi % (10**9 + 7)
