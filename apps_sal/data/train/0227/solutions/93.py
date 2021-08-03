import bisect


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        ans = 0
        countzeroes = 0
        prefix = []
        for i, num in enumerate(A):
            prefix.append(countzeroes)
            if num == 0:
                countzeroes += 1
            j = bisect.bisect_left(prefix, countzeroes - K)
            ans = max(ans, i - j + 1)
        return ans
