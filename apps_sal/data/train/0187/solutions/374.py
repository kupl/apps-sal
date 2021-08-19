class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        cur = 0
        ans = -1
        cur_p = 0
        prev = 0
        temp = 0
        n = len(customers)
        for i in range(n):
            cur += customers[i]

            if cur >= 4:
                cur_p = (prev + 4) * boardingCost - (i + 1) * runningCost
                prev += 4
                cur -= 4
            elif cur < 4:
                cur_p += (prev + cur) * boardingCost - (i + 1) * runningCost
                prev += cur
                cur = 0
            if cur_p > temp:
                ans = i + 1
                temp = cur_p

        if cur > 0:
            m = cur // 4
            for i in range(m + 1):
                # print(cur)
                if cur >= 4:
                    cur_p = (prev + 4) * boardingCost - (i + 1 + n) * runningCost
                    prev += 4
                    cur -= 4
                elif cur < 4:
                    # print(prev+cur)
                    # print(i+1+n)
                    cur_p = (prev + cur) * boardingCost - (i + 1 + n) * runningCost

                    prev += cur
                    cur = 0
                if cur_p > temp:
                    ans = i + 1 + n
                    temp = cur_p
                # print(cur_p)
                # print(\" \")
        return ans
