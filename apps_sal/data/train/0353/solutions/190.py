class Solution:
    def numSubseq(self, A: List[int], t: int) -> int:
        A, n = sorted(A), len(A)
        mod = (10 ** 9 + 7)
        ret = 0
        left, right = 0, n - 1
        while left <= right:
            while right >= left and A[left] + A[right] > t:
                right -= 1
            if right >= left and A[left] + A[right] <= t:
                ret += 2 ** (right - left) % mod
            left += 1
        return ret % mod
