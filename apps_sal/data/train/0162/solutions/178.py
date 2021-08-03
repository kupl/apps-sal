class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def memo(f):
            dic = {}

            def f_alt(*args):
                if args not in dic:
                    dic[args] = f(*args)
                return dic[args]
            return f_alt

        @memo
        def long(i, j):
            if i == -1 or j == -1:
                return 0
            return max(long(i - 1, j), long(i, j - 1), long(i - 1, j - 1) + (text1[i] == text2[j]))

        return long(len(text1) - 1, len(text2) - 1)
