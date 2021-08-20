from collections import Counter


class Solution:

    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        res = 0
        left = right = 0
        window = Counter()
        while right < len(A) and len(window) < K:
            window[A[right]] += 1
            right += 1
        if len(window) < K:
            return 0
        while right < len(A) and len(window) == K:
            rmarker = right
            while right < len(A) and A[right] in window:
                right += 1
            rcount = right - rmarker + 1
            lmarker = left
            while window[A[left]] > 1:
                window[A[left]] -= 1
                left += 1
            lcount = left - lmarker + 1
            res += lcount * rcount
            window[A[left]] -= 1
            del window[A[left]]
            left += 1
            right = rmarker
            while right < len(A) and len(window) < K:
                window[A[right]] += 1
                right += 1
        while len(window) == K:
            window[A[left]] -= 1
            res += 1
            if not window[A[left]]:
                del window[A[left]]
            left += 1
        return res
