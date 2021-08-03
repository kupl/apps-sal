class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        counts = [0] * 121
        for age in ages:
            counts[age] += 1
        SUM = 0
        sums = []
        for c in counts:
            SUM += c
            sums.append(SUM)
        res = 0
        for age in range(15, 121):
            up = age
            down = age // 2 + 7
            res += counts[age] * (sums[up] - sums[down] - 1)
        return res
