class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        avg, N = sum(A), len(A)
        if N < 2: return False
        if N == 2: return A[0] == A[1]
        A = [num*N - avg for num in A]
        
        dp = collections.defaultdict(set)
        # Last element goes to another array
        for i, n in enumerate(A[:-1]):
            if n == 0: return True # Single element array
            if i == 0:
                dp[0].add(n)
                continue
            sums = set()
            sums.add(n)
            for j, s in dp.items():
                for ps in s:
                    if ps + n == 0:
                        return True
                    sums.add(ps+n)
            dp[i] = sums
        return False
