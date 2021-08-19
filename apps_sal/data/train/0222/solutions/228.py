class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        n = len(A)
        ret = 0
        a_set = set(A)
        for i in range(n):
            for j in range(i + 1, n):
                num_1 = A[i]
                num_2 = A[j]
                length = 2
                while num_1 + num_2 in a_set:
                    num_3 = num_1 + num_2
                    num_1 = num_2
                    num_2 = num_3
                    length += 1
                if length > 2:
                    ret = max(ret, length)
        return ret
