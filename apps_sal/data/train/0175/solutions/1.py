class Solution:
    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """
        f = [0 for i in range(32)]
        f[0] = 1
        f[1] = 2
        for i in range(2, 32):
            f[i] = f[i - 1] + f[i - 2]
        ans = 0
        numL = list(map(int, bin(num)[2:]))
        l = len(numL)
        for i, n in enumerate(numL):
            if n == 1:
                ans += f[l - i - 1]
                if i > 0 and numL[i - 1] == 1:
                    return ans
        return ans + 1
