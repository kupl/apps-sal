class Solution:

    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:

        def solve(idx, counter):
            if idx == len(words):
                return 0
            wc = collections.Counter(words[idx])
            if all((counter[key] >= wc[key] for key in wc)):
                return max(sum((score[ord(c) - ord('a')] for c in words[idx])) + solve(idx + 1, counter - wc), solve(idx + 1, counter))
            else:
                return solve(idx + 1, counter)
        return solve(0, collections.Counter(letters))
