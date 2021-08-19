"""
The subproblem here is: suffixes

"abcde"
"ce"

So becase first letter "a" is in both text, its 1 plus the lcs of "bcde" and "ace"

if its not the same however, we try take suffix of both and see which one matches, we return longest 


"""


class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        memo = {}

        def lcs(pointer1, pointer2):
            if (pointer1, pointer2) in memo:
                return memo[pointer1, pointer2]
            if pointer1 >= n1 or pointer2 >= n2:
                return 0
            if text1[pointer1] == text2[pointer2]:
                x = 1 + lcs(pointer1 + 1, pointer2 + 1)
            else:
                x = max(lcs(pointer1 + 1, pointer2), lcs(pointer1, pointer2 + 1))
            memo[pointer1, pointer2] = x
            return x
        return lcs(0, 0)
