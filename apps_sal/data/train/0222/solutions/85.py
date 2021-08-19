class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        from collections import defaultdict
        used_tuples = set()
        max_len = 0
        hist = set(A)
        for i in range(len(A) - 1):
            for j in range(i + 1, len(A)):
                curr_len = 0
                s = A[i]
                l = A[j]
                if (s, l) in used_tuples:
                    continue
                while s + l in hist:
                    curr_len += 1
                    used_tuples.add((s, l))
                    old_s = s
                    s = l
                    l = s + old_s
                max_len = max(max_len, curr_len)
        return max_len + 2 if max_len > 0 else 0
