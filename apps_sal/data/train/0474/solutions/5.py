class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def letterScore(c):

            return score[ord(c) - ord('a')]

        def helper(i, remaining, scoreSoFar):
            if not remaining or i == len(words):
                return scoreSoFar

            # 1) Skip words[i]
            res = helper(i + 1, remaining, scoreSoFar)

            # 2) Take words[i] if possible
            cw = Counter(words[i])
            if not (cw - remaining):
                res = max(res, helper(i + 1, remaining - cw, scoreSoFar + sum(map(letterScore, words[i]))))

            return res

        return helper(0, Counter(letters), 0)

