class Solution:

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        '\n         if numRows==0:\n            return []\n         tem=[0,1]\n         l=[]\n         for i in range(numRows):\n            rowlist=[]\n             for j in range(len(tem)-1):\n                rowlist.append(tem[j]+tem[j+1])\n             l.append(rowlist)\n             tem=rowlist[:]\n             tem.insert(0,0)\n             tem.append(0)\n         return  l'
        ans = [[1] * n for n in range(1, numRows + 1)]
        for i in range(1, numRows + 1):
            for j in range(0, i - 2):
                ans[i - 1][1 + j] = ans[i - 2][j] + ans[i - 2][j + 1]
        return ans
