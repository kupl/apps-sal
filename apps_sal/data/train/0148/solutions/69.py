from itertools import chain
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        li = list(chain(zip(profit, difficulty)))
        li.sort()
        cutoffs = [li[-1][1]]
        profits = [li[-1][0]]
        for i in range(len(profit)-2, -1, -1):
            if li[i][1] < cutoffs[0]:
                cutoffs.insert(0, li[i][1])
                profits.insert(0, li[i][0])
        cutoffs.insert(0, 0)
        profits.insert(0, 0)
        ans = 0
        n = len(cutoffs)
        for ability in worker:
            l = 0
            r = n-1
            while(r >= l):
                mid = (l + r) // 2
                if ability == cutoffs[mid]:
                    break
                elif ability > cutoffs[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            mid = mid - 1
            for i in range(3):
                if mid+1 < n:
                    if ability >= cutoffs[mid+1]:
                        mid += 1
            ans += profits[mid]
        return(ans)
