class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        n = len(A)
        nums_on_left = set()
        max_seq_len = collections.defaultdict(lambda: 2)
        ans = 0
        for (i, c) in enumerate(A):
            for j in range(i - 1, 0, -1):
                b = A[j]
                a = c - b
                if a >= b:
                    break
                if a in nums_on_left:
                    max_seq_len[b, c] = max_seq_len[a, b] + 1
                    ans = max(ans, max_seq_len[b, c])
            nums_on_left.add(c)
        return ans
