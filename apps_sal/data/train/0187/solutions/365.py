class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        max_pro = -1
        shift = 0
        total_onboarded = 0
        wait = 0
        re = -1
        for c in customers:
            wait += c
            if wait > 0:
                shift += 1

                if wait > 4:
                    total_onboarded += 4
                else:
                    total_onboarded += wait

                cur_pro = total_onboarded * boardingCost - shift * runningCost
                if cur_pro > max_pro:
                    re = shift
                max_pro = max(max_pro, cur_pro)
                if wait > 4:
                    wait -= 4
                else:
                    wait = 0
            elif wait == 0:
                shift += 1
                cur_pro = total_onboarded * boardingCost - shift * runningCost
                continue

        # no more new customers
        while wait > 0:
            shift += 1

            if wait > 4:
                total_onboarded += 4
            else:
                total_onboarded += wait

            cur_pro = total_onboarded * boardingCost - shift * runningCost
            if cur_pro > max_pro:
                re = shift
            max_pro = max(max_pro, cur_pro)
            if wait > 4:
                wait -= 4
            else:
                wait = 0

        return re
