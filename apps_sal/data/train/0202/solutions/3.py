class Solution:

    def longestMountain(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        n = len(A)
        (ups, downs) = ([0] * n, [0] * n)
        (i, j) = (0, n - 1)
        while i < n - 1:
            if A[i] < A[i + 1]:
                ups[i + 1] = ups[i] + 1
            i += 1
        while j > 0:
            if A[j] < A[j - 1]:
                downs[j - 1] = downs[j] + 1
            j -= 1
        print((ups, downs))
        longest = [u + d + 1 for (u, d) in zip(ups, downs) if u and d]
        return max(longest) if longest else 0
