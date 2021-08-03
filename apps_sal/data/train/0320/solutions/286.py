class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # l = len(nums)
        sol = nums
        cost = 0
        # print(len(sol))
        while sum(sol) > 0:
            for i in range(len(sol)):
                # print(sol[i]&1)
                if sol[i] & 1 != 0:
                    sol[i] -= 1
                    cost += 1
            # print('sol after odd flip :',sol)
            if len(sol) > 0:
                sol = [x // 2 for x in sol if x > 0]
                if len(sol) > 0:
                    cost += 1
            # print('sol after /2 :',sol)
        return cost
