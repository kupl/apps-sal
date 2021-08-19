class Solution:

    def minOperationsMaxProfit(self, customers: List[int], bc: int, rc: int) -> int:
        maxi = 0
        ans = -1
        r = 0
        curr = 0
        temp = 0
        for c in customers:
            r += 1
            curr += c
            temp += min(curr, 4)
            curr -= min(curr, 4)
            if maxi < temp * bc - rc * r:
                maxi = temp * bc - rc * r
                ans = r
        while curr:
            r += 1
            temp += min(curr, 4)
            curr -= min(curr, 4)
            if maxi < temp * bc - rc * r:
                maxi = temp * bc - rc * r
                ans = r
        return ans
