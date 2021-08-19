class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = matrix
        ml = len(m)
        if ml == 0:
            return []
        nl = len(m[0])
        ms, me, ns, ne = 0, ml - 1, 0, nl - 1
        ans = []
        while ns <= ne or ms <= me:
            # print(ms,me,ns,ne)
            if ms <= me:
                for j in range(ns, ne + 1):
                    ans.append(m[ms][j])
                ms += 1
            # print(ms,me,ns,ne)
            if ne >= ns:
                for j in range(ms, me + 1):
                    ans.append(m[j][ne])
                ne -= 1
            # print(ms,me,ns,ne)
            if me >= ms:
                for j in range(ne, ns - 1, -1):
                    ans.append(m[me][j])
                me -= 1
            # print(ms,me,ns,ne)
            if ns <= ne:
                for j in range(me, ms - 1, -1):
                    ans.append(m[j][ns])
                ns += 1
            # print(ms,me,ns,ne)
        return ans
