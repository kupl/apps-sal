class Solution:
    def part(self, A, i, K, cache):
        if i < 0:
            if K == 0:
                return 0
            return float('-Inf')
        if i == 0:
            if K != 1:
                return float('-Inf')
            return A[i]
        key = '{}-{}'.format(i, K)
        if key in cache:
            return cache[key]
        res = float('-Inf')
        sm = 0
        count = 0
        for j in range(i, -1, -1):
            sm += A[j]
            count += 1
            avg = float(sm) / float(count)
            res = max(res, avg + self.part(A, j-1, K-1, cache))
        cache[key] = res
        return res
    
    def solve(self, A, K):
        return self.part(A, len(A)-1, K, {})
    
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        return self.solve(A, K)
