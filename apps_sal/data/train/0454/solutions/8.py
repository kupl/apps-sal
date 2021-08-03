class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        array = list(map(lambda x: int(x), str(num)))
        stack = []
        l = float('inf')
        r = None
        for i, d in enumerate(array):
            while stack and array[stack[-1]] < d:
                l = min(l, stack.pop())
            stack.append(i)
            if l < float('inf'):
                if not r or array[r] <= d:
                    r = i
        if l == float('inf'):
            return num
        else:
            basel = 10 ** (len(array) - 1 - l)
            baser = 10 ** (len(array) - 1 - r)
            return num + basel * (array[r] - array[l]) + baser * (array[l] - array[r])
