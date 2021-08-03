class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        points_L = []
        points_R = []

        for p in cardPoints:
            if len(points_L):
                points_L.append(points_L[-1] + p)
            else:
                points_L.append(p)
        for p in cardPoints[::-1]:
            if len(points_R):
                points_R.append(points_R[-1] + p)
            else:
                points_R.append(p)
        points_R = points_R[::-1]

        return self.solution(points_L, points_R, k)

    def solution(self, points_L, points_R, k):
        max = 0
        for i in range(k + 1):
            cmp1 = points_L[i - 1] if i > 0 else 0
            cmp2 = points_R[-(k - i)] if i < k else 0
            score = cmp1 + cmp2
            if score > max:
                max = score
        return max
