class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        n = len(A)
        if n == 0:
            return 0

        head = 0
        tail = 0
        num_zeros = 0
        max_subseq = 0
        while head < n:
            if A[head] == 1:
                head += 1
            else:
                num_zeros += 1
                max_subseq = max(max_subseq, head - tail)
                if num_zeros > K:
                    while A[tail] == 1:
                        tail += 1
                    tail += 1
                    num_zeros -= 1
                head += 1
        max_subseq = max(max_subseq, n - tail)
        return max_subseq
