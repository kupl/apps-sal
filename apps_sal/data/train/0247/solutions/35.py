class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        MAX = float('inf')
        n = len(arr) + 1
        best_till = [MAX for i in range(n + 1)]  # best subarray length until reach index i (exclusive)
        presum = 0
        maps = {}  # key: sum, val: index
        maps[0] = -1
        ans = best = MAX
        for i, v in enumerate(arr):
            presum += v
            # check if we have a subarray
            key = presum - target
            if key in maps:
                left_idx = maps[key]  # sums(arr[left_idx+1:i+1])
                curr_len = i - left_idx
                best = min(best, curr_len)

                # check if this could be a second subarray
                if left_idx > -1:
                    first_len = best_till[left_idx]
                    ans = min(ans, first_len + curr_len)

            best_till[i] = best
            maps[presum] = i

        if ans == MAX:
            return -1
        return ans
