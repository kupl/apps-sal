class Solution:
    def numOfSubarrays(self, a: List[int], k: int, threshold: int) -> int:
        lo, sum_of_win, cnt, target = -1, 0, 0, k * threshold
        for hi, v in enumerate(a):
            sum_of_win += v
            if hi - lo == k:
                if sum_of_win >= target:
                    cnt += 1
                lo += 1   
                sum_of_win -= a[lo]
        return cnt

