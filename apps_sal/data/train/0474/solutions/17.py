class Solution:

    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def solve(idx, counter):
            if idx == len(words):
                return 0

            wc = collections.Counter(words[idx])
            if all(counter[key] >= wc[key] for key in wc):
                ans = max(sum(score[ord(c) - ord('a')] for c in words[idx]) + solve(idx + 1, counter - wc), solve(idx + 1, counter))
            else:
                ans = solve(idx + 1, counter)

            return ans

        return solve(0, collections.Counter(letters))
