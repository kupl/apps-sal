class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        ans = cur = rem = 0
        prof = float('-inf')
        for idx, val in enumerate(customers):
            tmp = rem + val
            if tmp >= 4:
                cur += 4
                rem = tmp - 4
            else:
                cur += tmp
                rem = 0
            cur_prof = cur * boardingCost - runningCost * (idx + 1)
            if cur_prof > prof:
                prof = cur_prof
                ans = idx + 1
        if rem:
            rem_idx = rem // 4
            idx = len(customers) + rem_idx
            cur += rem - rem % 4
            cur_prof = cur * boardingCost - runningCost * (idx + 1)
            if cur_prof > prof:
                prof = cur_prof
                ans = idx

            if rem % 4:
                cur += rem % 4
                idx += 1
                cur_prof = cur * boardingCost - runningCost * (idx + 1)
                if cur_prof > prof:
                    prof = cur_prof
                    ans = idx
        return ans if prof > 0 else -1
