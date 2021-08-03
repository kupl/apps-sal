class Solution:
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        table = {}

        def helper(i):
            if i == 1:
                return 0
            if i in table:
                return table[i]
            if i % 2 == 0:
                return helper(i // 2) + 1
            table[i] = min(helper(i + 1), helper(i - 1)) + 1
            return table[i]
        return helper(n)
