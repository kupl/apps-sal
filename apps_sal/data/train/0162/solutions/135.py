class Solution:
    import functools
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        longest = 0
        memo = {}
        # represents the lcs of the substring text1[:i] and text2[:j]
        def calc_lcs(i, j):
            if i < 0 or j < 0: return 0
            if (i, j) in memo: return memo[(i, j)]
            # if the char at the end of the substring text1[:i] == text2[:j], then
            # we don't have to \"split out\" to search for the next common character, because we are already
            # there!. so simply return 1 + calclcs(i - 1, j - 1)
            if text1[i] == text2[j]: return 1 + calc_lcs(i - 1, j - 1)
            # however, if the char at the end of the subtring text1[:i] DOESNT equal the char at the end 
            # of the substring text2[:j], then we have to \"split out\", to try to find the next common 
            # character. For example, say we had the strings \"abcd\", and \"ac\". Clearly, 'c' doesn't equal 
            # 'd'. So what do we do? We have to try to find either the next occurence of 'd' in the 
            # second string, or the next occurence of 'c' in the first string. What if both occur?
            # well thats why we are taking the max! If both occur, it will result several \"lcs\"s being
            # calculuated, and we want the largest one!
            memo[(i, j)] = max(calc_lcs(i, j - 1), calc_lcs(i - 1, j))
            return memo[(i, j)]
        return calc_lcs(len(text1) - 1, len(text2) - 1)
            

