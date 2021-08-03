class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack_num = []
        stack_str = []
        num = ''
        string = ''
        for c in s:
            if c.isdigit():
                if num == '':
                    stack_str.append(string)
                    string = ''
                num += c
            elif c == '[':
                stack_num.append(int(num))
                num = ''
            elif c == ']':
                string = stack_str.pop() + string * stack_num.pop()
            else:
                string += c
        return string
