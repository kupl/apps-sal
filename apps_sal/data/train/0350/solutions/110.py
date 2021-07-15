class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        return self.helper(A, K) - self.helper(A, K-1)
        
    def helper(self, A, K):
        counter = collections.Counter()
        p1 = p2 = 0
        res = 0
        while p2 < len(A):
            if counter[A[p2]] == 0:
                K -= 1
            counter[A[p2]] += 1
            while K < 0:
                counter[A[p1]] -= 1
                if counter[A[p1]] == 0:
                    K += 1
                p1 += 1
            res += p2 - p1 + 1
            p2 += 1
        print(counter)
        return res
