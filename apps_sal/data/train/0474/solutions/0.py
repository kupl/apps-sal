class Solution:

    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        let = Counter(letters)
        sc = {}
        for i in range(26):
            sc[chr(i + ord('a'))] = score[i]
        word = {}
        for w in words:
            word[w] = Counter(w)
        self.ans = 0
        used = []

        def run(x, cur, let):
            if x == len(words):
                return
            for i in range(x, len(words)):
                if i not in used:
                    tmp = dict(let)
                    bx = True
                    d = 0
                    for (k, v) in word[words[i]].items():
                        if k not in let:
                            bx = False
                            break
                        let[k] -= v
                        d += sc[k] * v
                        if let[k] < 0:
                            bx = False
                            break
                    if bx:
                        used.append(i)
                        run(i + 1, cur + d, let)
                        if cur + d > self.ans:
                            self.ans = max(self.ans, cur + d)
                        used.pop()
                        let = tmp
                    let = tmp
        run(0, 0, let)
        return self.ans
