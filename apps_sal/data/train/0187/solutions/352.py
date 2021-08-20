class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        lines = []
        carry = 0
        cur = 0
        for c in customers:
            cur = 4 if c + carry >= 4 else c + carry
            carry = c + carry - 4 if c + carry > 4 else 0
            lines.append(cur)
        while carry:
            c = 4 if carry >= 4 else carry
            lines.append(c)
            carry = carry - 4 if carry > 4 else 0
        res = 0
        total = 0
        rotate = 0
        for (i, c) in enumerate(lines):
            total += c
            if total * boardingCost - (i + 1) * runningCost > res:
                res = total * boardingCost - (i + 1) * runningCost
                rotate = i + 1
        print(res)
        return rotate if res > 0 else -1
