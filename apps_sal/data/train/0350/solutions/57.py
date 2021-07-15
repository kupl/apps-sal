class Solution:
    def subarraysWithKDistinct(self, A: 'List[int]', K: 'int') -> 'int':
        freq = {}
        start = 0
        start_k = 0
        res = 0
        for i, x in enumerate(A):
            freq[x] = freq.get(x, 0) + 1
            if len(freq) == K + 1:
                # remove the distinct at start_k, move start_k, start
                del freq[A[start_k]]
                start_k += 1
                start = start_k
            if len(freq) == K:
                # update start_k and res (Notice: K >= 1)
                while freq[A[start_k]] > 1:
                    freq[A[start_k]] -= 1
                    start_k += 1
                res += start_k - start + 1
        return res
