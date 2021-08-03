class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        if len(A) == 0:
            return 0
        max_len_great = 1
        max_len_less = 1
        ans = 1
        for i in range(1, len(A)):
            if A[i - 1] < A[i]:
                max_len_great = max_len_less + 1
                max_len_less = 1
                ans = max(ans, max_len_great)
            elif A[i - 1] > A[i]:
                max_len_less = max_len_great + 1
                max_len_great = 1
                ans = max(ans, max_len_less)
            else:
                max_len_less = max_len_great = 1
        return ans
