class Solution:

    def subarraysWithKDistinct(self, A, K):
        return self.atMostK(A, K - 1) - self.atMostK(A, K)

    def atMostK(self, A, K):
        count = collections.Counter()
        ans = 0
        i = 0
        for j in range(len(A)):
            count[A[j]] += 1
            while len(count) > K:
                count[A[i]] -= 1
                if count[A[i]] == 0:
                    del count[A[i]]
                i += 1
            ans += i - j + 1
        return ans
