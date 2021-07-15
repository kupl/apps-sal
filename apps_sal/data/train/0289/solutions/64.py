class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        pref = [0] * (len(A)+1)
        for i in range(1, len(A)+1):
            pref[i] = pref[i-1] + A[i-1]
        l = [0] * (len(A)-L+1)
        m = [0] * (len(A)-M+1)
        for i in range(len(A)-L+1):
            l[i] = pref[i+L] - pref[i]
        for i in range(len(A)-M+1):
            m[i] = pref[i+M] - pref[i]
        ans = 0
        for i in range(len(l)):
            for j in range(i-M+1):
                ans = max(ans, l[i]+m[j])
            for j in range(i+L, len(A)-M+1):
                ans = max(ans, l[i]+m[j])
        return ans

