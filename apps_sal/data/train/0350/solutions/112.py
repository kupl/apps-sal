from collections import Counter


class Solution:

    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        window = Counter()
        res = 0
        left = right = 0
        while True:
            while right < len(A) and len(window) < K:
                window[A[right]] += 1
                right += 1
            if len(window) < K:
                return res
            j = right
            while j < len(A) and A[j] in window:
                j += 1
            res += j - right + 1
            window[A[left]] -= 1
            if not window[A[left]]:
                del window[A[left]]
            left += 1
        return res
