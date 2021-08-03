class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

#         def fac(num):
#             factorial = 1
#             for i in range(1, num+1):
#                 factorial *= i
#             return factorial

#         i = 1
#         L = []
#         while i <= numRows:
#             j = 1
#             l = []
#             while j <= i:
#                 l.append(int(fac(i-1)/(fac(j-1)*fac(i-j))))
#                 j += 1
#             L.append(l)
#             i += 1

#         return L


#         if numRows == 0:
#             return []

#         i = 1
#         L = [[1]]
#         while i+1 <= numRows:
#             j = 0
#             l = []
#             while j <= i:
#                 if j == 0 or j == i:
#                     l.append(1)
#                 else:
#                     l.append(L[i-1][j-1]+L[i-1][j])
#                 j += 1
#             L.append(l)
#             i += 1

#         return L

        # result = []
        # for i in xrange(numRows):
        #     result.append([])
        #     for j in xrange(i + 1):
        #         if j in (0, i):
        #             result[i].append(1)
        #         else:
        #             result[i].append(result[i - 1][j - 1] + result[i - 1][j])
        # return result

        # if not numRows: return []
        # res = [[1]]
        # for i in range(1, numRows):
        #     res += [list(map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1]))]
        # return res[:numRows]

        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        res = [[1], [1, 1]]

        def add(nums):
            res = nums[:1]
            for i, j in enumerate(nums):
                if i < len(nums) - 1:
                    res += [nums[i] + nums[i + 1]]
            res += nums[:1]
            return res

        while len(res) < numRows:
            # res.extend([add(res[-1])])
            res.append(add(res[-1]))
        return res
