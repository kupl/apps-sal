class Solution:

    def subarraysWithKDistinct(self, A, K):
        return self.atMostK(A, K) - self.atMostK(A, K - 1)

    def atMostK(self, A, K):
        count = collections.Counter()
        res = left = right = distinct = 0
        while right < len(A):
            count[A[right]] += 1
            if count[A[right]] == 1:
                distinct += 1
            while distinct > K:
                count[A[left]] -= 1
                if count[A[left]] == 0:
                    distinct -= 1
                left += 1
            res += right - left + 1
            right += 1
        return res
    '\n        for j in range(len(A)):\n            if count[A[j]] == 0: K -= 1\n            count[A[j]] += 1\n            while K < 0:\n                count[A[i]] -= 1\n                if count[A[i]] == 0: K += 1\n                i += 1\n            res += j - i + 1\n    '
