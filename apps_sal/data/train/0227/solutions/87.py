class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        ct = Counter()
        pt, max_len = 0, 0
        for i, elem in enumerate(A):
            ct[elem] += 1
            if ct[0] <= K:
                max_len = max(max_len, (i - pt + 1))
            if ct[0] > K:
                ct[A[pt]] -= 1
          
                pt += 1

        return max_len

