class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:

        start = 0
        ans = 0
        nn = [0, 0]

        for i, a in enumerate(A):
            nn[a] += 1
            while nn[0] > K:
                nn[A[start]] -= 1
                start += 1

            ans = max(ans, nn[0] + nn[1])
        return ans
