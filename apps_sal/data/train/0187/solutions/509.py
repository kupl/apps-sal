from collections import deque
class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        ans = [0]
        q = deque(customers)
        while len(q) > 0:
            cur = q.popleft()
            if cur > 4:
                r = cur - 4
                if len(q) > 0:
                    q[0] += r
                else:
                    q.append(r)
            profit = (min(cur, 4)*boardingCost-runningCost)
            ans.append(ans[-1]+profit)
        maxP = max(ans)
        # print(maxP, ans)
        maxTime = [i for i in range(len(ans)) if ans[i] == maxP][0]
        return -1 if maxP == 0 else maxTime
