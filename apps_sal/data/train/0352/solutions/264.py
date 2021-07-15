class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        explored = set()
        stack = [(word, 1) for word in sorted(words, key = len, reverse = True)]
        words = set(words)
        best = 1
        while stack:
            word, chain_length = stack.pop()
            best = max(best, chain_length)
            for candidate_word in [word[:i] + c + word[i:] for c in 'abcdefghijklmnopqrstuvwxyz' for i in range(len(word) + 1)]:
                if candidate_word in words and candidate_word not in explored:
                    stack.append((candidate_word, chain_length + 1))
                    explored.add(candidate_word)
        return best

