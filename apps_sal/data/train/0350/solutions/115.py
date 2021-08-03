class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        def remove(m, n):
            if m[n] == 1:
                del m[n]
            else:
                m[n] -= 1
        m1, m2 = collections.Counter(), collections.Counter()
        res = 0
        i1 = i2 = -1
        for i0, n in enumerate(A):
            while i1 + 1 < len(A) and len(m1) < K:
                i1 += 1
                m1[A[i1]] += 1
            if len(m1) < K:
                return res

            while i2 + 1 < len(A) and len(m2) < K + 1:
                i2 += 1
                m2[A[i2]] += 1

            res += i2 - i1 + int(len(m2) == K)
            remove(m1, n)
            remove(m2, n)
        return res
