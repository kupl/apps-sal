class Solution:

    def differ(self, x1, x2):
        (i, j) = (0, 0)
        diff = 0
        while i != len(x1) and j != len(x2):
            if x1[i] != x2[j]:
                diff += 1
            else:
                i += 1
            if diff > 1:
                return False
            j += 1
        return True

    def check(self, x1, x2):
        if x1 == x2:
            return True
        if abs(len(x1) - len(x2)) != 1:
            return False
        else:
            if len(x2) > len(x1):
                (a, b) = (x1, x2)
            else:
                (a, b) = (x2, x1)
            return self.differ(a, b)

    def longestStrChain(self, words: List[str]) -> int:
        words = list(set(words))
        lengths = {}
        for word in words:
            length = len(word)
            lengths[length] = lengths.get(length, []) + [word]
        lengths = sorted(lengths.items(), key=lambda x: x[0], reverse=True)
        value = {}
        max_chain = 1
        for (i, length) in enumerate(lengths):
            for word in length[1]:
                if i == 0:
                    value[word] = 1
                else:
                    temp_max = 0
                    for temp_word in lengths[i - 1][1]:
                        if self.check(word, temp_word):
                            temp_max = max(temp_max, value[temp_word])
                    value[word] = 1 + temp_max
                    max_chain = max(value[word], max_chain)
        return max_chain
