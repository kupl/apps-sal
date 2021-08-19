class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key=lambda x: len(x))
        pred = [1] * len(words)

        def diff1(w1, w2):
            for i in range(len(w2)):
                if w2[:i] + w2[i + 1:] == w1:
                    return True
            return False

        def diff2(w1, w2):
            i = 0
            while i < len(w1) and w1[i] == w2[i]:
                i += 1
            j = len(w1) - 1
            while j >= i and w1[j] == w2[j + 1]:
                j -= 1
            if j == i - 1:
                return True
            return False
        for i in range(len(words)):
            j = i - 1
            while j >= 0 and abs(len(words[j]) - len(words[i])) < 2:
                if len(words[j]) == len(words[i]) - 1 and diff2(words[j], words[i]):
                    pred[i] = max(pred[i], pred[j] + 1)
                j -= 1
        return max(pred)
