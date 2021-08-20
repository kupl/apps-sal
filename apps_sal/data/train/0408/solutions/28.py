class Solution:

    def findBestValue(self, A, target):

        def mutedSum(A, t):
            s = 0
            for x in A:
                s += min(x, t)
            return s
        (l, r) = (1, max(A))
        while l < r:
            m = (l + r) // 2
            cur = 0
            for x in A:
                cur += min(x, m)
            if cur <= target:
                l = m + 1
            else:
                r = m
        s1 = mutedSum(A, r)
        s2 = mutedSum(A, r - 1)
        return r if abs(target - s1) < abs(target - s2) else r - 1
