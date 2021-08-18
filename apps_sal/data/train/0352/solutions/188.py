class Solution:
    def check(self, word1, word2) -> bool:
        if len(word1) + 1 != len(word2):
            return False
        for i in range(len(word1) + 1):
            if i < len(word1) and word1[i] == word2[i]:
                continue
            else:
                word2 = word2[:i] + word2[i + 1:]
                return word1 == word2

    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        output = [0 for i in range(len(words))]
        for j in range(-1, -len(words) - 1, -1):
            temp_len = 1
            k = j + 1
            while k <= -1:
                if temp_len < output[k] + 1:
                    if self.check(words[j], words[k]):
                        temp_len = output[k] + 1
                k += 1
            output[j] = temp_len
        return max(output)
