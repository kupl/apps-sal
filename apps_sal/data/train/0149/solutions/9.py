class Solution:

    def removeDuplicates(self, s: str, k: int) -> str:
        ns = []
        deleted = True
        while deleted:
            deleted = False
            i = 0
            ns = []
            while i < len(s):
                if i <= len(s) - k and s[i + 1:i + k] == s[i] * (k - 1):
                    deleted = True
                    i += k
                else:
                    ns.append(s[i])
                    i += 1
            s = ''.join(ns)
        return s
