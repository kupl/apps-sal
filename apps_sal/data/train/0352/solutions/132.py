class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def determine(s1, s2):
            if len(s2) != len(s1) + 1:
                return False

            insert = False
            j = 0
            for i in range(len(s1)):
                while s2[j] != s1[i]:
                    if insert:
                        return False
                    j = j + 1
                    insert = True
                j = j + 1
            return True

        d = {}
        words = sorted(words, key=lambda x: len(x))
        d[words[-1]] = 1
        for i in reversed(list(range(len(words) - 1))):
            m = 0
            d[words[i]] = 1
            for j in range(i, len(words)):
                if determine(words[i], words[j]):
                    if d[words[j]] > m:
                        d[words[i]] = d[words[j]] + 1
                        m = d[words[i]]

        out = 0
        for k in d:
            if d[k] > out:
                out = d[k]

        return out
