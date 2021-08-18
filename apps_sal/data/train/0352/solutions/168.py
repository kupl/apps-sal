class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))
        max_len = [1] * len(words)
        res = 1
        for i in range(len(words) - 1):
            for j in range(i, len(words)):
                if self.isPredecessor(words[i], words[j]):
                    max_len[j] = max(max_len[i] + 1, max_len[j])
                    res = max(res, max_len[j])
        return res

    def isPredecessor(self, s1, s2):
        if len(s2) - len(s1) != 1:
            return False
        flag = 0
        i, j = 0, 0
        while i < len(s1) and j < len(s2):
            if s1[i] == s2[j]:
                i += 1
                j += 1
            elif flag == 0:
                flag = 1
                j += 1
            else:
                return False
        return True
