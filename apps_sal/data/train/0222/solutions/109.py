class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        setA = set(A)
        # overlapping=set()
        r = 0
        for i in range(len(A)):
            start = A[i]
            for j in range(i + 1, len(A) - 1):
                prev_prev = start
                prev = A[j]
                count = 0
                while prev + prev_prev in setA:
                    # overlapping.add(prev)
                    # overlapping.add(prev_prev)
                    prev_prev, prev = prev, prev + prev_prev
                    count += 1
                r = max(r, count)
        if r != 0:
            return r + 2
        else:
            return r
