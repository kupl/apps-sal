class Solution:
    def maxVowels(self, S, K):
        N = len(S)
        L = [0] * (N + 1)
        for i in range(N):
            if S[i] in ['a', 'e', 'i', 'o', 'u']:
                L[i + 1] = 1
        for i in range(1, N + 1):
            L[i] += L[i - 1]
        i = 0
        j = K
        ans = 0
        while(i <= N and j <= N):
            ans = max(ans, L[j] - L[i])
            i += 1
            j += 1
        return ans
