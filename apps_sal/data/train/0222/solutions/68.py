class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        set_val = set(A)
        max_len = 0
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                (p2, p1) = (A[i], A[j])
                cnt = 0
                while p2 + p1 in set_val:
                    z = p2 + p1
                    p2 = p1
                    p1 = z
                    cnt += 1
                max_len = max(max_len, cnt + 2 if cnt > 0 else cnt)
        return max_len
