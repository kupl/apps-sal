class Solution:
    Dmap = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if '1' in digits or '0' in digits:
            return []
        if len(digits) == 0:
            return []
        return self.letterC(digits)

    def letterC(self, digits):
        if len(digits) == 0:
            return ['']
        res = []
        for back in self.letterC(digits[1:]):
            for fr in self.Dmap[digits[0]]:
                res.append(fr + back)
        return res
