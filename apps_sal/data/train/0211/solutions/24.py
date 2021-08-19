class Solution:

    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        maxi = 0

        def sub(ind, ar):
            if ind == n:
                if len(ar) == len(set(ar)):
                    return len(ar)
                return maxi
            a = ar + [s[ind]]
            b = ar[:]
            b[-1] += s[ind]
            return max(sub(ind + 1, a), sub(ind + 1, b))
        return sub(1, [s[0]])
