import collections
class Solution:
    def atMostK(self, A, K):
        count = collections.Counter()
        i, ans = 0, 0 # i is left pointer of window, j is right
        for j in range(len(A)):
            if count[A[j]] == 0:
                K -= 1  # K keeps track of # of different chars in the window
            count[A[j]] += 1
            while K < 0: # when there are too many different chars, contract window
                count[A[i]] -= 1
                if count[A[i]] == 0: # when A[i] is no longer in the window
                    K += 1
                i += 1
            ans += j - i + 1 # for each new A[j], we add j - i + 1 substrings
        return ans
        
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        return self.atMostK(A, K) - self.atMostK(A, K - 1)
        
        
    # exactly(K) = atMost(K) - atMost(K-1)
    # why j - i + 1? For [a, b, c, d] and K = 3, for atMostK, a -> [a], b -> [b], [a, b], c -> [c], [b, c], [a, b, c], d -> [d], [c, d], [b, c, d] every time we look at a new item we add the length of window to total count

