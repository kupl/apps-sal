class Solution:
    def __init__(self):
        self.phone = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if not digits:
            return []

        results = []
        self.dfs(digits, results, "", 0)
        return results

    def dfs(self, digits, results, string, index):
        if index == len(digits):
            results.append(string)
        else:
            letters = self.phone[int(digits[index])]

            for i in range(0, len(letters)):
                self.dfs(digits, results, string + letters[i], index + 1)
