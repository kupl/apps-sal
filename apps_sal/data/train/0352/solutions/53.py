class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def predecessor(word1, word2):
            for i in range(len(word2)):
                if word2[0:i] + word2[i + 1:] == word1:
                    return True
            return False
        words.sort(key=len)
        words_sort = {}
        for i in words:
            if len(i) in words_sort:
                words_sort[len(i)].append(i)
            else:
                words_sort[len(i)] = [i]

        def dfs(words, words_sort):
            max_chain = 1
            stack = [(1, word) for word in words[::-1]]
            while stack:
                current = stack.pop()
                if current[0] > max_chain:
                    max_chain = current[0]
                if len(current[1]) + 1 in words_sort:
                    for word in words_sort[len(current[1]) + 1]:
                        if predecessor(current[1], word):
                            if (1, word) in stack:
                                stack.remove((1, word))
                            stack.append((current[0] + 1, word))
                else:
                    continue
            return max_chain
        max_chain = dfs(words, words_sort)
        return max_chain
