class Solution:

    def minCost(self, s: str, cost: List[int]) -> int:
        (left, right) = (0, 1)
        costSum = 0
        while right < len(s):
            if s[left] == s[right]:
                while right < len(s) and s[left] == s[right]:
                    right += 1
                tmp = cost[left:right]
                maxIndex = tmp.index(max(tmp))
                for i in range(len(tmp)):
                    if i != maxIndex:
                        costSum += tmp[i]
                left = right
                right += 1
            else:
                left += 1
                right += 1
        return costSum
