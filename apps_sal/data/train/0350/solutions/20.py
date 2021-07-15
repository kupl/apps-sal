class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        
        def atMost(K):
            N = len(A)
            ct = collections.Counter()
            ans = 0
            i = 0
            for j in range(N):
                ct[A[j]] += 1
                if len(ct) <= K:
                    ans += j - i + 1
                else:
                    while len(ct) > K:
                        ct[A[i]] -= 1
                        if ct[A[i]] == 0: del ct[A[i]]
                        i += 1
                    ans += j - i + 1
            return ans
        
        return atMost(K) - atMost(K-1)

