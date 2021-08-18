class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        start = 0
        end = L
        t = sum(A[start:end])
        maxs = 0
        while end < len(A) + 1:
            pin1 = 0
            end1 = M
            tot = sum(A[pin1:end1])
            while end1 < start + 1:
                if t + tot > maxs:
                    maxs = t + tot
                tot = tot - A[pin1]
                tot = tot + A[end1]
                pin1 += 1
                end1 += 1
            pin2 = end
            end2 = end + M
            tot2 = sum(A[pin2:end2])
            while end2 <= len(A):
                if t + tot2 > maxs:
                    maxs = t + tot2
                if end2 == len(A):
                    break
                tot2 = tot2 - A[pin2]
                tot2 = tot2 + A[end2]
                pin2 += 1
                end2 += 1
            if end == len(A):
                break
            t = t - A[start]
            t = t + A[end]
            start += 1
            end += 1
        return maxs
