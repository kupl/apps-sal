class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0

        prev_height = None
        peaks = [0 for _ in range(len(A))]
        has_increment = False

        # combs left to right for peaks
        for idx in range(len(A)):
            if prev_height is not None:
                if prev_height < A[idx]:
                    peaks[idx] = peaks[idx - 1] + 1
                    has_increment = True
                else:
                    if has_increment:
                        peaks[idx - 1] += 1
                    peaks[idx] = 0
                    has_increment = False
            prev_height = A[idx]

        print(peaks)

        # combs right to left for peaks
        prev_height = None
        max_so_far = 0
        has_increment = False

        for idx in range(len(A) - 1, -1, -1):
            if prev_height is not None:
                if prev_height < A[idx]:
                    peaks[idx] += peaks[idx + 1] + 1
                    has_increment = True
                else:
                    if has_increment and prev_height > A[idx]:
                        max_so_far = max(max_so_far, peaks[idx + 1])
                    peaks[idx] = peaks[idx]
                    has_increment = False
            prev_height = A[idx]

        print(peaks)

        return max_so_far
