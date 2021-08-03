class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        ans, pos = 0, 0

        for _, v in itertools.groupby(s):
            v = list(v)
            if len(v) > 1:
                to_sort = []
                for x in range(len(v)):
                    to_sort.append(cost[pos])
                    pos += 1
                ans += sum(sorted(to_sort)[:-1])
            else:
                pos += 1

        return ans
