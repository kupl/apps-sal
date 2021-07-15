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
            res += (right - left) + 1
            right += 1
        return res
    '''
        for j in range(len(A)):
            if count[A[j]] == 0: K -= 1
            count[A[j]] += 1
            while K < 0:
                count[A[i]] -= 1
                if count[A[i]] == 0: K += 1
                i += 1
            res += j - i + 1
    '''
