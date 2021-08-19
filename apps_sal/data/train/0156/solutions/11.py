class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # Step 1. find a longest common subsequence.
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def helper(i, j):  # longest common subseq of str1[:i+1] and str2[:j+1]
            if i == 0:
                if str1[0] == str2[j]:
                    return str1[0]
                elif j == 0:
                    return ''
                else:
                    return helper(i, j - 1)
            if j == 0:
                if str1[i] == str2[0]:
                    return str2[0]
                else:
                    return helper(i - 1, j)
            # i>0, j>0
            if str1[i] == str2[j]:
                return helper(i - 1, j - 1) + str1[i]
            else:
                return max(helper(i - 1, j), helper(i, j - 1), key=len)

        subseq = helper(len(str1) - 1, len(str2) - 1)

        # Step 2. make a supersequences from the longest common subsequence.
        ans, i, j = '', 0, 0
        for c in subseq:
            while i < len(str1) and str1[i] != c:
                ans += str1[i]
                i += 1
            while j < len(str2) and str2[j] != c:
                ans += str2[j]
                j += 1
            ans += c
            i += 1
            j += 1
        return ans + str1[i:] + str2[j:]
