class Solution:
    def countTriplets(self, A: List[int]) -> int:

        dp = collections.defaultdict(int)
        for n1 in A:
            for n2 in A:
                dp[n1 & n2] += 1

        res = 0
        for n in A:
            for k, v in dp.items():
                if not k & n:
                    res += v
        return res
