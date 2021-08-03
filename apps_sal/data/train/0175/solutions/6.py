class Solution:
    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 3:
            return num + 1
        if num == 3:
            return num
        import math
        bits = int(math.log(num, 2))
        f = [0] * (bits + 1)
        f[0], f[1], f[2] = 2, 3, 4
        for i in range(3, bits + 1):
            f[i] = f[i - 1] + f[i - 2] - 1

        res = 0
        pre = 0
        flag = False
        for i in range(bits + 1):
            if num & (1 << i):

                if pre:
                    res = f[i] + f[i - 1] - 2

                elif flag:
                    res = f[i] + res - 1
                else:
                    res = f[i] + res
                    flag = True
            pre = num & (1 << i)
            # print(pre)
        return res
