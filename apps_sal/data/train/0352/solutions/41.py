class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        if not words:
            return

        dic = {}
        result = 1

        for word in sorted(words, key=len):
            dic[word] = 1

            for i in range(len(word)):
                currWord = word[:i] + word[i + 1:]

                if currWord in dic:
                    dic[word] = max(dic[word], dic[currWord] + 1)
                    result = max(result, dic[word])

        return result
