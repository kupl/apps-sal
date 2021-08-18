class Solution:
    def minOperations(self, nums: List[int]) -> int:
        sol = nums
        cost = 0
        while sum(sol) > 0:
            for i in range(len(sol)):
                if sol[i] & 1 != 0:
                    sol[i] -= 1
                    cost += 1
            if len(sol) > 0:
                sol = [x // 2 for x in sol if x > 0]
                if len(sol) > 0:
                    cost += 1
        return cost
