class Solution:
    def longestPrefix(self, s: str) -> str:
        #         prefixes = []
        #         for i in range(1, len(s)):
        #             prefixes.append(s[0:i])

        #         # print(prefixes)

        #         suffixes = []
        #         for i in range(1, len(s)):
        #             suffixes.append(s[len(s)-i:])

        #         # print(suffixes)

        #         common = set(prefixes).intersection(set(suffixes))

        #         # print(common)

        #         ans = ''
        #         for s in common:
        #             if len(s) > len(ans):
        #                 ans = s
        #         return ans
        i = 1
        ans = ''
        while i < len(s):
            # print(s[0:i], s[len(s)-i:])
            if s[0:i] == s[len(s) - i:]:
                ans = s[0:i]
            i += 1
        return ans
