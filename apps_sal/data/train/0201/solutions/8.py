class Solution:

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = [1]
        i = 1
        while i < n:
            tmp = [sum(a), sum(a)]
            for j in range(len(a) - 1):
                tmp.append(tmp[j + 1] - a[j])
            i += 1
            a = tmp
        return sum(a)
