class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        def atMost(S):
            ans, l, tmp = 0, 0, 0

            for r in range(len(A)):
                tmp = tmp + A[r]
                while (tmp > S and l <= r):
                    tmp = tmp - A[l]
                    l = l + 1
                ans += r - l + 1
            return ans

        return atMost(S) - atMost(S - 1)
