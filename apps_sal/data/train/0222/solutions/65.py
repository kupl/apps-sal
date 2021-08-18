class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        exists = set(A)
        max_length = 2

        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                a = A[i]
                b = A[j]
                curr_length = 2

                while (a + b) in exists:
                    curr_length += 1
                    a, b = b, a + b
                max_length = max(max_length, curr_length)

        if max_length <= 2:
            return 0
        return max_length
