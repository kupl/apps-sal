class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        d = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            cur_max = 0
            for kk in range(1, k + 1):
                if i - kk + 1 < 0:
                    continue
                cur_max = max(cur_max, arr[i - kk + 1])
                d[i] = max(d[i], d[i - kk] + cur_max * kk)
        print(d)
        return d[-2]
