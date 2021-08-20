class Solution:

    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if num == '':
            return ''
        arr = [i for i in list(num)]
        stack = [arr[0]]
        out = 0
        for i in range(1, len(arr)):
            while out < k and len(stack) > 0 and (arr[i] < stack[-1]):
                stack.pop()
                out += 1
            stack.append(arr[i])
        diff = k - out
        for i in range(diff):
            stack.pop()
        res = ''.join(stack).lstrip('0')
        if res == '':
            return '0'
        return res
