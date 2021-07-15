class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        length = len(A)

        # Stores [difference, index] -> length
        # for each position j:
        #   the arithmetic sequence 
        hash = {}

        for i in range(length):
            for j in range(i + 1, length):
                hash[A[j] - A[i], j] = hash.get((A[j] - A[i], i), 1) + 1

        # O(n)
        return max(hash.values())
