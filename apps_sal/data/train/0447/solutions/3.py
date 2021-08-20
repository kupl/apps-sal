class Solution:

    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        str_index = {char: i for (i, char) in enumerate(s)}
        result = ''
        for (i, char) in enumerate(s):
            if char not in result:
                while char < result[-1:] and i < str_index[result[-1]]:
                    result = result[:-1]
                result += char
        return result
