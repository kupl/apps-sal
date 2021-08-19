class Solution:

    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        table = [[None for i in range(len(nums))] for j in range(len(nums))]
        for i in range(len(nums)):
            table[i][i] = (nums[i], str(nums[i]))
        return self.findmax(table, 0, len(nums) - 1)[1]

    def findmax(self, table, i, j):
        if table[i][j] is not None:
            return table[i][j]
        if j - i == 1:
            (a, a_s) = table[i][i]
            (b, b_s) = table[j][j]
            ret = (a / b, a_s + '/' + b_s)
            table[i][j] = ret
            return ret
        m = -1
        ret = None
        for d in range(i, j):
            (ma, max_rep) = self.findmax(table, i, d)
            (mi, min_rep) = self.findmin(table, d + 1, j)
            div = ma / mi
            if div > m:
                m = div
                ret = (max_rep, min_rep)
        rep = self.assemble(ret[0], ret[1])
        print('max %d, %d: v, %f, %s' % (i, j, m, rep))
        ret = (m, rep)
        table[i][j] = ret
        return ret

    def findmin(self, table, i, j):
        if table[j][i] is not None:
            return table[j][i]
        if j - i == 1:
            (a, a_s) = table[i][i]
            (b, b_s) = table[j][j]
            ret = (a / b, a_s + '/' + b_s)
            table[j][i] = ret
            return ret
        m = float('inf')
        ret = None
        for d in range(i, j):
            (ma, max_rep) = self.findmin(table, i, d)
            (mi, min_rep) = self.findmax(table, d + 1, j)
            div = ma / mi
            if div < m:
                m = div
                ret = (max_rep, min_rep)
        rep = self.assemble(ret[0], ret[1])
        print('min %d, %d: v, %f, %s' % (i, j, m, rep))
        ret = (m, rep)
        table[j][i] = ret
        return ret

    def assemble(self, up, down):
        if '/' in down:
            return '%s/(%s)' % (up, down)
        else:
            return '%s/%s' % (up, down)
