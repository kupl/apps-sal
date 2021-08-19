class Solution:
    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """
        dp = [1, 2]
        for i in range(2, 32):
            dp.append(dp[i - 1] + dp[i - 2])

        bnum = bin(num)[2:]
        size = len(bnum)
        ans = dp[size]
        for i in range(1, size):
            if bnum[i - 1] == bnum[i] == '1':
                # 关键 娥娥 对 因为他就是一个二进制数在这儿循环呢
                # 所以他可以这样
                break
            if bnum[i - 1] == bnum[i] == '0':
                ans -= dp[size - i] - dp[size - i - 1]
                # 其实问题就是在于这儿 是在干什么 为什么会有这么一部 算了 先记住
        return ans
