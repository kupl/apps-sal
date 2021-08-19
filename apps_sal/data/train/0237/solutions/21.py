class Solution:

    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        n = len(A)
        prefix = [0 for _ in range(n + 1)]
        for i in range(n):
            prefix[i + 1] = prefix[i] + A[i]

        def at_most_k(k: int) -> int:
            (begin, end) = (0, 1)
            cnt = 0
            while end < n + 1:
                while begin < end and prefix[end] - prefix[begin] > k:
                    begin += 1
                cnt += end - begin
                end += 1
            return cnt
        return at_most_k(S) - at_most_k(S - 1)
