class Solution:

    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        (d, t) = (defaultdict(int), defaultdict(int))
        (a, b) = (K, K)
        (left, right) = (0, 0)
        res = 0
        for (i, ele) in enumerate(A):
            a -= 1 if d[ele] == 0 else 0
            b -= 1 if t[ele] == 0 else 0
            d[ele] += 1
            t[ele] += 1
            while a < 0:
                a += 1 if d[A[left]] == 1 else 0
                d[A[left]] -= 1
                left += 1
            while b <= 0:
                b += 1 if t[A[right]] == 1 else 0
                t[A[right]] -= 1
                right += 1
            res += right - left
        return res
