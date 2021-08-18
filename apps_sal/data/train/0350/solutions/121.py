class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        m1, m2 = collections.Counter(), collections.Counter()

        def remove(m, n):
            m[n] -= 1
            if not m[n]:
                del m[n]

        res = 0
        left = right = -1
        for i, n in enumerate(A):
            while left < len(A) - 1 and len(m1) < K:
                left += 1
                m1[A[left]] += 1

            if len(m1) < K:
                return res

            while right < len(A) - 1 and len(m2) <= K:
                right += 1
                m2[A[right]] += 1

            res += right - left + (len(m2) == K)
            remove(m1, n)
            remove(m2, n)
        return res
