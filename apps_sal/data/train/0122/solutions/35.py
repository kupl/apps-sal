class Solution:
    def maxScore(self, cardPoints, k: int) -> int:
        N = len(cardPoints)
        preS, afterS = [0]*(N+1), [0]*(N+1)
        ans = 0
        for i in range(1,N+1):
            preS[i]=preS[i-1]+cardPoints[i-1]
        for j in range(1,N+1):
            afterS[j] = afterS[j-1]+cardPoints[N-j]
        for l in range(k+1):
            ans = max(ans,preS[l]+afterS[k-l])
        return ans
