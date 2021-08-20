class Solution:

    def longestStrChain(self, words: List[str]) -> int:

        def check(s, t):
            (m, n) = (len(s), len(t))
            flag = False
            j = 0
            if n != m + 1:
                return False
            for i in range(n):
                if j < m and t[i] == s[j]:
                    j += 1
                elif not flag:
                    flag = True
                else:
                    return False
            return True
        words = sorted(words, key=lambda entry: len(entry), reverse=False)
        table = [1] * len(words)
        for i in range(1, len(table)):
            maxVal = 0
            for j in range(i):
                if len(words[j]) + 1 == len(words[i]) and check(words[j], words[i]) and (table[i] < table[j] + 1):
                    table[i] = table[j] + 1
        return max(table)
