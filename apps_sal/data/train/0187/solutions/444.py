class Solution:
    def minOperationsMaxProfit(self, customers: List[int], bc: int, rc: int) -> int:
        if 4 * bc <= rc:
            return -1
        ans = -1
        p = 0
        pre = 0
        i = 0
        r = 1
        while i < len(customers):
            slot = 0
            while slot < 4 and i < r and i < len(customers):
                if customers[i] <= 4 - slot:
                    slot += customers[i]
                    i += 1
                else:
                    customers[i] -= (4 - slot)
                    slot = 4
            pre += slot
            v = pre * bc - r * rc
            if p < v:
                ans = r
                p = v
            r += 1
        return ans
