class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        max_score = 0
        word_limits = Counter(letters)

        def helper(curr, chars, curr_words):
            nonlocal max_score
            if curr >= len(words):
                if chars & word_limits == chars:
                    curr_score = sum([chars[c] * score[ord(c) - 97] for c in chars])
                    max_score = max(max_score, curr_score)
                    print(chars)
            else:
                chars += Counter(words[curr])
                helper(curr + 1, chars, curr_words + 1)
                chars -= Counter(words[curr])
                helper(curr + 1, chars, curr_words)
        helper(0, Counter(), 0)
        return max_score
