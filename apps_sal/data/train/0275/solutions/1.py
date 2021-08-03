class Solution:
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        rem = {}

        def dfs(i, c):
            if c < 0:
                return False
            elif i == len(s):
                return not c
            elif (i, c) in rem:
                return rem[(i, c)]
            else:
                if s[i] == '(':
                    rem[(i, c)] = dfs(i + 1, c + 1)
                elif s[i] == ')':
                    rem[(i, c)] = dfs(i + 1, c - 1)
                else:
                    rem[(i, c)] = dfs(i + 1, c) or dfs(i + 1, c - 1) or dfs(i + 1, c + 1)
            return rem[(i, c)]
        return dfs(0, 0)
