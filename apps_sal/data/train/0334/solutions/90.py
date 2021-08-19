from heapq import nsmallest


class Solution:

    def minCost(self, s: str, cost: List[int]) -> int:
        if len(s) < 2:
            return 0
        (left, right) = (0, 1)
        res = 0
        window = dict()
        while right < len(s):
            if s[right] != s[left]:
                right += 1
                left += 1
                continue
            print(left)
            while right < len(s) and s[right] == s[left]:
                right += 1
            res += sum(nsmallest(right - left - 1, cost[left:right]))
            left = right
            right += 1
        return res
