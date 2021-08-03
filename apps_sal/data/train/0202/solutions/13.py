class Solution:
    def longestMountain(self, A: List[int]) -> int:
        # edge case
        if len(A) == 0:
            return 0

        n = len(A)
        peak = None
        maxMountainLen = 0

        i = 1
        while (i + 1) < n:
            if A[i - 1] < A[i] and A[i] > A[i + 1]:
                # already obtained the peak
                left = right = i

                while (left - 1) >= 0 and A[left - 1] < A[left]:
                    left -= 1

                while (right + 1) < n and A[right + 1] < A[right]:
                    right += 1

                # max length of mountain
                maxMountainLen = max(maxMountainLen, right - left + 1)
                i = right + 1
            else:
                i += 1

        return maxMountainLen
