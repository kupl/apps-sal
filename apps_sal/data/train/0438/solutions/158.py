class Solution:

    # def findLatestStep(self, arr: List[int], m: int) -> int:
    def fstep(self, arr, start_idx, end_idx, step, m):
        # u can't hit end idx
        n = end_idx - start_idx
        if n == m:
            return step + 1
        turnoff = arr[step] - 1
        if turnoff < start_idx or turnoff >= end_idx:
            return self.fstep(arr, start_idx, end_idx, step - 1, m)

        left = turnoff - start_idx
        right = n - left - 1

        lr = -1
        rr = -1
        if left >= m:
            lr = self.fstep(arr, start_idx, start_idx + left, step - 1, m)
        if right >= m:
            rr = self.fstep(arr, start_idx + left + 1, end_idx, step - 1, m)

        return max(lr, rr)

    def findLatestStep(self, arr: List[int], m: int) -> int:
        return self.fstep(arr, 0, len(arr), len(arr) - 1, m)
