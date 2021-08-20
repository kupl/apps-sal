class Solution:

    def longestOnes(self, A: List[int], K: int) -> int:
        l = 0
        r = 0
        m = len(A)
        count = 0
        max_count = 0
        while r < m:
            if A[r] == 1:
                count += 1
            while r - l + 1 - count > K:
                if A[l] == 1:
                    count -= 1
                l += 1
            max_count = max(r - l + 1, max_count)
            r += 1
        return max_count
