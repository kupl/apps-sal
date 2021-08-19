class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        nums = [v for v in s]
        res = 0
        flag = 0
        d = collections.defaultdict(set)
        i = 1
        while i < len(nums):
            while 0 <= i < len(nums) and nums[i] == nums[i - 1]:
                d[flag].add(i)
                d[flag].add(i - 1)
                i += 1
            flag += 1
            i += 1

        for v in d.values():
            # print(v)
            print(v)
            curr_cost = [cost[c] for c in v]
            max_val = max(curr_cost)
            res += sum(curr_cost)
            print(max_val)
            res -= max_val
        return res
