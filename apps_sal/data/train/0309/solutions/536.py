class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:

        if not A:
            return 0

        dp = {}

        for it1 in range(1, len(A)):

            for it2 in range(it1):

                key_tuple = (it2, A[it1] - A[it2])

                if key_tuple not in dp:
                    dp[(key_tuple)] = 1

                dp[(it1, A[it1] - A[it2])] = dp[(key_tuple)] + 1
        return max(dp.values())
