class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        s_len = len(s)
        if s_len == 0:
            return True

        found = [True]
        for ind in range(s_len):
            if_found = False
            for i in range(ind + 1):
                # print(len(found)-i-1)
                # print(s[(len(found)-i-1):(ind+1)])
                if found[len(found) - i - 1] and s[(len(found) - i - 1):(ind + 1)] in wordDict:
                    found += [True]
                    break
            if len(found) == ind + 1:
                found += [False]
        print(found)
        return found[-1]
