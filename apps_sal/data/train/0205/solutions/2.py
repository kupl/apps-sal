class Solution:

    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """

        def getMax(arr, m, n):
            res = 0
            for e in arr:
                if m >= e[0] and n >= e[1]:
                    res += 1
                    m -= e[0]
                    n -= e[1]
            return res
        arr = [(s.count('0'), s.count('1')) for s in strs]
        arr1 = sorted(arr, key=lambda s: -min(m - s[0], n - s[1]))
        arr2 = sorted(arr, key=lambda s: min(s[0], s[1]))
        res = max(getMax(arr1, m, n), getMax(arr2, m, n))
        return res
