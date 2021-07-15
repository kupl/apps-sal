class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = defaultdict(lambda: 1)
        for first_index in range(len(A) - 1):
            for second_index in range(first_index + 1, len(A)):
                dp[(second_index, A[second_index] - A[first_index]
                    )] = dp[(first_index, A[second_index] - A[first_index])] + 1
        max_length = max(dp.values())
        return max_length

