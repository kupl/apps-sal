class Solution:
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 特殊判断
        if n <= 0:
            return 0
        # 先得到输入数字n的位数
        i = 0
        while pow(10, i) <= n:
            i += 1
        if i == 1:
            return 1

        # 递归得到1～s之间所有的1值
        s = n % pow(10, i - 1)
        temp = self.countDigitOne(s)

        # 再得到s+1～n之间所有的1值
        # 先得到最高位为1的所有1值
        t = n // pow(10, i - 1)
        if t > 1:
            temp1 = pow(10, i - 1)
        elif t == 1:
            temp1 = s + 1
        # 再得到其它位为1的所有1值
        temp2 = t * (i - 1) * pow(10, i - 2)
        return temp + temp1 + temp2
