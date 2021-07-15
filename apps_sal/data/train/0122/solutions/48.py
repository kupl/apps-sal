class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        f, b = [0], [0]
        for n in cardPoints:
            f.append(f[-1] + n)
        for n in cardPoints[::-1]:
            b.append(b[-1] + n)
        allCombo = [f[i] + b[k-i] for i in range(k+1)]
        return max(allCombo)

