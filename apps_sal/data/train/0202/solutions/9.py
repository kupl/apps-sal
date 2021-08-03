class Solution:
    def longestMountain(self, A: List[int]) -> int:
        idx = 0
        big = 0
        while idx + 1 < len(A):
            long = 1
            if A[idx + 1] > A[idx]:
                while idx + 1 < len(A) and A[idx + 1] > A[idx]:
                    idx += 1
                    long += 1
            else:
                idx += 1
                continue
            if idx + 1 < len(A) and A[idx + 1] < A[idx]:
                while idx + 1 < len(A) and A[idx + 1] < A[idx]:
                    idx += 1
                    long += 1
            else:
                idx += 1
                continue
            big = max(long, big)
        return big if big >= 3 else 0
