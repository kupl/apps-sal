class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        res = sorted([(speed[i], efficiency[i]) for i in range(n)], key=lambda x: [-x[1], -x[0]])

        num = 0
        sums = []
        ss = 0
        maxi = 0
        for s, e in res:
            if num < k:
                heappush(sums, s)
                ss += s
                num += 1
                maxi = max(maxi, ss * e)
            else:
                rmv = heappushpop(sums, s)
                ss = ss - rmv + s
                maxi = max(maxi, ss * e)

        return maxi % (10**9 + 7)
