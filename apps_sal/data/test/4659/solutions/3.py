class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        '''
         if numRows==0:
            return []
         tem=[0,1]
         l=[]
         for i in range(numRows):
            rowlist=[]
             for j in range(len(tem)-1):
                rowlist.append(tem[j]+tem[j+1])
             l.append(rowlist)
             tem=rowlist[:]
             tem.insert(0,0)
             tem.append(0)
         return  l'''
        ans = [[1] * n for n in range(1, numRows + 1)]
        for i in range(1, numRows + 1):
            for j in range(0, i - 2):
                ans[i - 1][1 + j] = ans[i - 2][j] + ans[i - 2][j + 1]
        return ans
