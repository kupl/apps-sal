class Solution:

    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        lcnt = Counter(letters)
        words = [w for w in words if all((Counter(w)[l] <= lcnt[l] for l in w))]
        al = 'abcdefghijklmnopqrstuvwxyz'
        scores = {w: sum((score[al.index(l)] for l in w)) for w in words}
        costs = {w: Counter(w) for w in words}
        score = 0
        for i in range(1, len(words) + 1):
            for comb in combinations(words, i):
                if all((sum((costs[w][l] for w in comb)) <= lcnt[l] for l in lcnt)):
                    score = max(score, sum((scores[w] for w in comb)))
        return score
