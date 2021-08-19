class Solution:

    def minCost(self, n: int, cuts: List[int]) -> int:
        self.memo = {}
        self.helper(0, n, cuts)
        return self.memo[0, n]

    def helper(self, left, right, candidates):
        if left >= right:
            return 0
        if (left, right) in self.memo:
            return self.memo[left, right]
        res = sys.maxsize
        for k in candidates:
            if k <= left or k >= right:
                continue
            left_cost = self.helper(left, k, candidates)
            right_cost = self.helper(k, right, candidates)
            cost = right - left
            res = min(res, left_cost + right_cost + cost)
        if res == sys.maxsize:
            res = 0
        self.memo[left, right] = res
        return res
