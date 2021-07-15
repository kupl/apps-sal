from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, A, K):
        def atMostK(K):
            cnt, res, i = defaultdict(int), 0, 0
            for j, val in enumerate(A):
                cnt[val] += 1
                while len(cnt) > K:
                    X = A[i]
                    cnt[X] -= 1
                    if not cnt[X]: cnt.pop(X)
                    i += 1
                res += j - i + 1
            return res       
        return atMostK(K) - atMostK(K-1)
