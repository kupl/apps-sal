class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # Sorting words by length is necessary
        words.sort(key=lambda x: len(x))
        max_len = [1] * len(words)
        res = 1
        for i in range(len(words) - 1):
            for j in range(i, len(words)):
                if self.isPredecessor(words[i], words[j]):
                    max_len[j] = max(max_len[i] + 1, max_len[j])
                    res = max(res, max_len[j])
        return res

    # Use this function to check whether s1 is a predecessor of s2
    def isPredecessor(self, s1, s2):
        # Corner case:
        if len(s2) - len(s1) != 1:
            return False
        # Use flag to record whether difference between s1 and s2 is found
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
