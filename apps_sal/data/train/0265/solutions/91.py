class Solution:
    def maxNonOverlapping(self, A: List[int], T: int) -> int:
        N = len(A)
        prefix_sum = [0 for _ in range(N + 1)]
        for i in range(1, N + 1):
            prefix_sum[i] = prefix_sum[i - 1] + A[i - 1]
        seen = set([0])
        res = 0
        for i in range(N):
            curr = prefix_sum[i + 1]
            want = curr - T
            if want in seen:
                res += 1
                seen = set()
            seen.add(curr)
        return res
