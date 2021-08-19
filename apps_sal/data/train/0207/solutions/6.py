class Solution:

    def sorting(self, numstr):
        newnumstr = []
        for i in range(0, len(numstr)):
            for j in range(1, len(numstr) - i):
                if numstr[j - 1] + numstr[j] < numstr[j] + numstr[j - 1]:
                    temp = numstr[j - 1]
                    numstr[j - 1] = numstr[j]
                    numstr[j] = temp

    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        matrix = dict()
        for num in nums:
            numstr = str(num)
            if numstr[0] not in matrix:
                matrix[numstr[0]] = []
            matrix[numstr[0]].append(numstr)
        print(matrix)
        ret = ''
        for i in range(9, -1, -1):
            if str(i) in matrix:
                prenums = matrix[str(i)]
                self.sorting(prenums)
                ret += ''.join(prenums)
        return str(int(ret))
