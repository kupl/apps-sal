class Solution:

    def maxLength(self, arr: List[str]) -> int:
        res = 0
        unique = ['']

        def isvalid(s):
            return len(s) == len(set(s))

        for word in arr:
            for u in unique:
                tmp = word + u
                if isvalid(tmp):
                    unique.append(tmp)
                    res = max(res, len(tmp))

        return res
