class Solution:

    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        i = 0
        num += '0'
        while i < len(num):
            while stack and stack[-1] > num[i] and (k > 0):
                stack.pop()
                k -= 1
            if (stack or num[i] != '0') and i < len(num) - 1:
                stack.append(num[i])
            i += 1
        res = ''.join(stack)
        return res if res else '0'
