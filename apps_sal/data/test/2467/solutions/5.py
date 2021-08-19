class Solution:

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if n > 45:
            return []
        res = []

        def rev(start, s, count, one):
            if count == k and s == n:
                res.append(one[:])
                return
            if count == k or s == n:
                return
            for i in range(start, 10):
                if s + i > n:
                    return
                rev(i + 1, s + i, count + 1, one + [i])
        rev(1, 0, 0, [])
        return res
