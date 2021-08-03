class Solution:
    def decodeString(self, s):
        count = ''
        res = ''
        count_stack = []
        res_stack = []

        for i in range(len(s)):
            if ord('0') <= ord(s[i]) <= ord('9'):
                count += s[i]
            elif s[i] == '[':
                count_stack.append(int(count) if count else 0)
                res_stack.append(res)
                count = ''
                res = ''
            elif s[i] == ']':
                res = res_stack.pop() + res * count_stack.pop()
            else:
                res += s[i]
        return res
