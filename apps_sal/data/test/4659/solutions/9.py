class Solution:

    def my_fact(self, n):
        if n == 1 or n == 0:
            return 1
        else:
            return n * self.my_fact(n - 1)

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[] for i in range(numRows)]
        for n in range(numRows):
            for k in range(0, n + 1):
                val = self.my_fact(n) / (self.my_fact(n - k) * self.my_fact(k))
                res[n].append(int(val))
        return res
