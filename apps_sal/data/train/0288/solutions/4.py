class Solution:

    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        if m == 0:
            return 1
        lights = [True] * n
        if m > 4:
            if m & 1:
                m = 3
            else:
                m = 4
        return self.final(m, lights)

    def operate(self, num, array):
        if num == 1:
            array = [not i for i in array]
        elif num == 2:
            for i in range(len(array)):
                if i & 1:
                    array[i] = not array[i]
        elif num == 3:
            for i in range(len(array)):
                if not i & 1:
                    array[i] = not array[i]
        elif num == 4:
            for i in range(len(array)):
                if i % 3 == 0:
                    array[i] = not array[i]
        return array

    def final(self, num, array):
        ops = [[[1], [2], [3], [4]], [[], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], [[1], [2], [3], [4], [1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]], [[], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4], [1, 2, 3, 4]]]
        res = []
        for op in ops[num - 1]:
            tmp = array.copy()
            if not op:
                res.append(tmp)
            else:
                for i in op:
                    tmp = self.operate(i, tmp)
                if not tmp in res:
                    res.append(tmp)
        return len(res)
