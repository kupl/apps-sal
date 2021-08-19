class Solution:

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if not digits:
            return []
        res = []
        self.dfs(digits, 0, '', res)
        return res

    def dfs(self, digits, index, path, res):
        if len(path) == len(digits):
            res.append(path)
            return
        for i in range(len(self.dic[digits[index]])):
            path_ = path + self.dic[digits[index]][i]
            self.dfs(digits, index + 1, path_, res)
