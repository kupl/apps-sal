class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        m = len(s)
        if m == 0:
            return ''
        result = []
        for i in s:
            if i != ']':
                result.append(i)
            else:
                char_temp = []
                r1m = len(result)
                for j in range(r1m - 1, -1, -1):
                    if result[j] != '[':
                        char_temp.insert(0, result.pop())
                    else:
                        result.pop()
                        break

                digit_char = []
                r2m = len(result)
                for j in range(r2m - 1, -1, -1):
                    if result[j].isdigit():
                        digit_char.insert(0, result.pop())
                    else:
                        break
                result += char_temp * (int(''.join(digit_char)))
        return ''.join(result)
