class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        return self.atMost(A, K) - self.atMost(A,K-1)
    
    def atMost(self, A, K):
        if K == 0: return 0
        hi, res = 0, 0
        n = len(A)
        count = collections.defaultdict(int)
        for lo in range(n):
            while hi < n  and (len(count) < K or A[hi] in count):
                count[A[hi]] += 1
                hi += 1
            res += hi - lo
            count[A[lo]] -= 1
            if count[A[lo]] == 0:
                count.pop(A[lo])
        return res

