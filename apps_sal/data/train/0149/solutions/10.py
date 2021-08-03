class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        def helper(s):

            ans = []

            i = 0
            while i < len(s):

                if s[i] * k != s[i:i + k]:
                    ans.append(s[i])
                    i += 1
                else:
                    i += k

            if len(ans) == len(s):
                res.append(''.join(ans))
                return
            else:
                helper(''.join(ans))

        res = []
        helper(s)
        return res[0]
