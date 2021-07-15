class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        contains = lambda w1, w2: all(l1 in w2 for l1 in w1)
        
        words.sort(key=lambda a: len(a))
        n = len(words)
        chain = [1] * n
        for i in range(n):
            j = i+1
            while j < n and len(words[j]) == len(words[i]):
                j += 1
            while j < n and len(words[j]) == len(words[i]) + 1:
                if contains(words[i], words[j]) and chain[i] + 1 > chain[j]:
                    chain[j] = chain[i] + 1
                j += 1
        
        return max(chain)
